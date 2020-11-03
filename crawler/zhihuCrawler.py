#!/bin/python3

from selenium import webdriver
import re
import random
import time
import os

class zhihuCrawler:
    def __init__(self, dataDir=None, crawledQuestionsFilePath=None, errorQuestionFilePath=None, debug=False):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        self.browser = webdriver.Firefox(profile)
        
        if dataDir == None:
            self.dataDir = os.path.dirname(os.path.abspath(__file__)) + '/data/zhihu/' # not working dir
        elif not(os.path.exists(dataDir) and os.path.isdir(dataDir)):
            print("invalid dir: %s" % dataDir)
            return
        else:
            self.dataDir = dataDir

        if self.dataDir[-1] != '/':
            self.dataDir += '/'
        
        self.crawledQuestionsList = []
        self.crawledQuestionsFile = self.openFile(crawledQuestionsFilePath, self.dataDir + "crawledQuestions")
        for line in self.crawledQuestionsFile:
            try:
                if int(line) not in self.crawledQuestionsList:
                    self.crawledQuestionsList.append(int(line))
            except:
                print("'%s' can not be converted to a question id")

        self.errorQuestionsList = []
        self.errorQuestionsFile = self.openFile(errorQuestionFilePath, self.dataDir + "errorQuestions")
        for line in self.errorQuestionsFile:
            try:
                if int(line) not in self.errorQuestionsList:
                    self.errorQuestionsList.append(int(line))
            except:
                print("'%s' can not be converted to a question id")

        self.cookieSetted = False
        self.debug = debug

    def openFile(self, path, defaultPath):
        try:
            f = open(path, "r+")
        except:
            try:
                f = open(path, "w+")
            except:
                try:
                    f = open(defaultPath, "r+")
                except:
                    f = open(defaultPath, "w+")
                    return f
                else:
                    return f
            else:
                return f
        else: 
            return f

    def __del__(self):
        self.browser.close()
        if self.crawledQuestionsFile != None:
            self.crawledQuestionsFile.close()

    def addCookie(self, cookieString):    
        cookieString = cookieString.replace(' ', '')
        self.browser.get('https://www.zhihu.com')
        try:
            for oneCookie in cookieString.split(';'):
                key, value = oneCookie.split('=', 1)
                self.browser.add_cookie({'name': key, 'value': value})
        except:
            print("cookie set error")
        else:
            self.cookieSetted = True
        finally:
            self.browser.get("about:blank")

    def clearCookie(self):
        self.browser.delete_all_cookies()
        self.cookieSetted = False

    def getQuestions(self, hot=False, pullDownTimes=0):
        if self.cookieSetted == False:
            print("You need to login to get questions, addCookie() should be called first")
            return
        
        if hot == True:
            outFileName = "hotQuestions"
            questionUrl = "https://www.zhihu.com/hot"
        else:
            outFileName = "questions"
            questionUrl = "https://www.zhihu.com/"

        try:
            self.browser.get(questionUrl)
        except:
            print("Fail to get %s" % questionUrl)
            return

        try:
            outFile = open(self.dataDir + outFileName, "r+")
        except:
            outFile = open(self.dataDir + outFileName, "w+")

        curQidList = []
        for line in outFile:
            curQidList.append(int(line))

        if hot == True:
            questions = self.browser.find_elements_by_xpath("//a[starts-with(@href, 'https://www.zhihu.com/question/') and @title and not(@class)]")
        else:
            for i in range(pullDownTimes):
                sleepTime = random.randint(2000, 4000) / 1000
                time.sleep(sleepTime)
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight - 2000)")
            questions = self.browser.find_elements_by_xpath("//a[starts-with(@href, '//www.zhihu.com/question/') and @data-za-detail-view-element_name='Title']")    

        for oneQuestion in questions:
            qId = int(re.search("www.zhihu.com/question/([0-9]*)", oneQuestion.get_attribute("href"))[1])
            if qId not in curQidList:
                curQidList.append(qId)
                outFile.write(str(qId) + '\n')
        outFile.close()

    def getAnswersOfQuestionsInFile(self, filePath, rawHTML=False, urlParsing=False, interlval=5):
        try:
            questionFile = open(filePath, "r")
        except:
            print("can't open %s" % filePath)
            return

        questionList = []
        for line in questionFile:
            try:
                qId = int(line)
            except ValueError:
                print("%s is not a number")
                questionFile.close()
                return
            
            questionList.append(qId)

        for qId in questionList:
            crawled = self.getAnswersOfOneQuestion(qId, rawHTML=rawHTML, urlParsing=urlParsing)
            if crawled != -1:
                time.sleep(interlval)

        questionFile.close()

    def getAnswersOfOneQuestion(self, qId, rawHTML=False, urlParsing=False):
        if qId in self.crawledQuestionsList or qId in self.errorQuestionsList:
            print("question %s has been crawled" % qId)
            return -1

        if self.debug == True:
            print("-----------------------------------------------------")
        print("Start crawling question %s" % qId)

        try:
            self.browser.get("https://www.zhihu.com/question/%s" % qId)
        except:
            print("Fail to get https://www.zhihu.com/hot")
            return

        # close login window
        if self.cookieSetted == False:
            self.browser.execute_script("window.scrollTo(0, 2500)")
            time.sleep(4)
            try:
                closeButton = self.browser.find_element_by_xpath("//button[@class='Button Modal-closeButton Button--plain']")
            except:
                if self.debug == True:
                    print("This question may be locked, it is added to the error list")
                self.errorQuestionsList.append(qId)
                self.errorQuestionsFile.write(str(qId) + '\n')

                return -1
            else:
                closeButton.click()
                if self.debug == True:
                    print("Login window has been closed")
            self.browser.execute_script("window.scrollTo(0, 0)")

        oldScrollHeight = self.browser.execute_script("return document.body.scrollHeight")
        # pull down to many times will cause the program to crash
        for i in range(100):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight - 2000)")
            sleepTime = random.randint(2000, 4000) / 1000
            time.sleep(sleepTime)
            newScrollHeight = self.browser.execute_script("return document.body.scrollHeight")
            if oldScrollHeight == newScrollHeight:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight - 1500)")
                time.sleep(5)
                newScrollHeight = self.browser.execute_script("return document.body.scrollHeight")
                if oldScrollHeight == newScrollHeight:
                    break
                else:
                    oldScrollHeight = newScrollHeight
            else:
                oldScrollHeight = newScrollHeight

        if self.debug == True:
            print("Pull down finished, oldScrollHeight is %s, newScrollHeight is %s" % (oldScrollHeight, newScrollHeight))

        time.sleep(10)
        answers = self.browser.find_elements_by_xpath("//span[@class='RichText ztext CopyrightRichText-richText' and @itemprop='text']")
        if self.debug == True:
            lastAnswerContent = answers[-1].text
        upvotes = self.browser.find_elements_by_xpath("//button[@class='Button VoteButton VoteButton--up']")

        if self.debug == True:
            print("The number of answers is %s" % len(answers))
            print("Content of last question is:")
            print(lastAnswerContent)

        # problem1: fetch() function can not be triggered by the scrollIntoView() js function
        # problem2: although fetch() is triggered mannuly, curLastAnswer can not be referred because the DOM tree is modified
        # answers = self.browser.find_elements_by_xpath("//span[@class='RichText ztext CopyrightRichText-richText' and @itemprop='text']")
        # while True:
        #     curLastAnswer = answers[-1]
        #     self.browser.execute_script("arguments[0].scrollIntoView();", curLastAnswer)
        #     newAnswers = curLastAnswer.find_elements_by_xpath("following::span[@class='RichText ztext CopyrightRichText-richText' and @itemprop='text']")
        #     if newAnswers == []:
        #         break
        #     else:
        #         answers.extend(newAnswers)

        contentFile = open(self.dataDir + "%s.content" % qId, "w")
        if urlParsing:
            urlFile = open(self.dataDir + "%s.url" % qId, "w")

        for i in range(len(answers)):
            contentFile.write("ANSWER%s:\n" % i)
            
            try:
                contentFile.write(re.search("[0-9]+", upvotes[i].get_attribute("aria-label"))[0] + '\n')
            except Exception as err:
                print(repr(err))
                answers = self.browser.find_elements_by_xpath("//span[@class='RichText ztext CopyrightRichText-richText' and @itemprop='text']")
                upvotes = self.browser.find_elements_by_xpath("//button[@class='Button VoteButton VoteButton--up']")
                # print(answers[-1].text)
                # print(len(answers))
                # print(len(upvotes))
                # input()
                # print(upvotes[-1].get_attribute("outerHTML"))
                # input()
                # contentFile.write(re.search("[0-9]+", upvotes[i].get_attribute("aria-label"))[0] + '\n')
                # input()

            if rawHTML:
                contentFile.write(answers[i].get_attribute("innerHTML") + '\n')
            else:
                contentFile.write(answers[i].text + '\n')

            if urlParsing:
                urlList = answers[i].find_elements_by_xpath("descendant::a")
                urlFile.write("ANSWER%s:\n" % i)
                for url in urlList:
                    urlFile.write(url.get_attribute("outerHTML") + '\n')
        
        contentFile.close()
        if urlParsing:
            urlFile.close()

        self.crawledQuestionsList.append(qId)
        self.crawledQuestionsFile.write(str(qId) + '\n')

        print("Finish crawling question %s" % qId)

class zhihuDataAnalyzer:
    def __init__(self, dataDir=""):
        self.dataDir = dataDir
        if self.dataDir != "" and self.dataDir[-1] != '/':
            self.dataDir += '/'

    def analyzeQuestionsInFile(self, filePath, printRes=True, debug=False):
        try:
            qFile = open(self.dataDir + filePath, "r")
        except:
            print("can not open %s" % self.dataDir + filePath)
            return -1

        qList = []
        for line in qFile:
            if int(line) not in qList:
                qList.append(int(line))

        answerNum = 0
        urlNum = 0
        httpNum = 0
        httpsNum = 0
        stats = {}

        for qId in qList:
            ret = self.analyzeOneQuestion("%s.url" % qId, debug=debug)
            if ret != -1:
                stats[qId] = ret

                answerNum += stats[qId][0]
                urlNum += stats[qId][1]
                httpNum += stats[qId][2]
                httpsNum += stats[qId][3]

        if printRes == True:
            print("|%+20s|%+15s|%+15s|%+15s|%+15s|" % ("questionID", "total answers", "total urls", "http urls", "https urls"))
            print("-" * 86)
            for qId in stats:
                print("|%+20s|%+15s|%+15s|%+15s|%+15s|" % (qId, stats[qId][0], stats[qId][1], stats[qId][2], stats[qId][3]))
            print("|%+20s|%+15s|%+15s|%+15s|%+15s|" % ("total:", answerNum, urlNum, httpNum, httpsNum))

        return answerNum, urlNum, httpNum, httpsNum, stats

    def analyzeOneQuestion(self, filePath, debug=False):
        try:
            urlFile = open(self.dataDir + filePath, "r")
        except:
            print("can not open %s" % self.dataDir + filePath)
            return -1

        answerNum = 0
        urlNum = 0
        httpNum = 0
        httpsNum = 0
        firstTimeFlag = True
        for line in urlFile:
            if line[:6] == "ANSWER":
                answerNum += 1
                continue

            try:
                url = re.search("href=\"(.*)\"", line)[1]
            except TypeError:
                continue

            if "link.zhihu.com" in url:
                url = url[len("https://link.zhihu.com/?target="):]

            if url[:7] == "http%3A" or url[:5] == "http:":
                httpNum += 1
            elif url[:5] == "https" or url[0:2] == "//":
                httpsNum += 1
            else:
                if debug == True:
                    if firstTimeFlag == True:
                        print("------------------------------------")
                        print(filePath)
                        print("------------------------------------")
                        firstTimeFlag = False
                    print("answer %s: %s" % (answerNum, url))
            
            urlNum += 1

        return answerNum, urlNum, httpNum, httpsNum

if __name__ == "__main__":
    # crawler = zhihuCrawler(debug=True)
    # cookieString = '_zap=49515c31-8d17-46ad-83ef-72fe146e5b8b; d_c0="AKDR3iB_CBKPTsNv9KRQFiOO7OY1vsVADg8=|1602587842"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1602748146,1602748228,1603270215,1603271401; capsion_ticket="2|1:0|10:1603271401|14:capsion_ticket|44:MDkyMzE4MjY2NWMwNDAxZDgzNzllNDAzNGYxMWQwNGM=|cb3aa401359ee784d23698871191908369288d724c94533852b088640f62c360"; tst=r; tshl=; q_c1=843142f3dc544de6be6e16ce35a451b3|1602673668000|1602673668000; _xsrf=AobudXCq8sVrSnVA7X37o9lxpkJjDTPE; KLBRSID=ca494ee5d16b14b649673c122ff27291|1603271436|1603271400; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1603271426; SESSIONID=cXp1RFFLx6genAiFNtQIGeEoWgRm6OSRPxzdB1M3ag9; JOID=WlAdCkLjbfSHDInfL-LMp9sp99Y9gDWFtl_PmWKaW5PjYsm2aQqWetkNid4uae9hC4bjGmmjh5E0fcZ1W4A8M1o=; osd=UFkdCk7pZPSHAIPWL-LArdIp99o3iTWFulXGmWKWUZrjYsW8YAqWdtMEid4iY-ZhC4rpE2mji5s9fcZ5UYk8M1Y=; z_c0="2|1:0|10:1603271424|4:z_c0|92:Mi4xcHV1X0F3QUFBQUFBb05IZUlIOElFaVlBQUFCZ0FsVk5BRWw5WUFEQXA5b3N3QjJYeTlrQTJtSGNsbnlkbS1HdVR3|f3956da6c18ae820b7829b2a4ac6fd1c8edc123ea6fdb4357ccc017706b2ab47"; unlock_ticket="AADCdIW76womAAAAYAJVTQgCkF87VnwdO2vaeIzzwu9ykizSkl1s2Q=="'
    # crawler.addCookie(cookieString)
    # crawler.getQuestions(pullDownTimes=100)
    # crawler.getAnswersOfQuestionsInFile("./data/zhihu/questions", rawHTML=True, urlParsing=True)
    # crawler.getAnswersOfOneQuestion(412123743, rawHTML=True, urlParsing=True)
    analyzer = zhihuDataAnalyzer(dataDir="./data/zhihu")
    analyzer.analyzeQuestionsInFile("crawledQuestions", debug=True)


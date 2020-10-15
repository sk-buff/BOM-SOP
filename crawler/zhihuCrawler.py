#!/bin/python3

from selenium import webdriver
import re
import random
import time
import os

class zhihuCrawler:
    def __init__(self, dataDir=None, crawledQuestionsFilePath=None):
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
        self.crawledQuestionsFile = None
        if crawledQuestionsFilePath != None:
            try:
                self.crawledQuestionsFile = open(crawledQuestionsFilePath, "r+")
            except:
                print("can not open %s" % crawledQuestionsFilePath)
            else:
                for line in self.crawledQuestionsFile:
                    self.crawledQuestionsList.append(int(line))

        self.cookieSetted = False

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
            qId = re.search("www.zhihu.com/question/([0-9]*)", oneQuestion.get_attribute("href"))[1]
            if qId not in curQidList:
                outFile.write(qId + '\n')
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

    def getAnswersOfOneQuestion(self, qId, rawHTML=False, urlParsing=False, outputInfo=True):
        if qId in self.crawledQuestionsList:
            if outputInfo == True:
                print("question %s has been crawled" % qId)
            return -1

        try:
            self.browser.get("https://www.zhihu.com/question/%s" % qId)
        except:
            print("Fail to get https://www.zhihu.com/hot")
            return

        # close login window
        if self.cookieSetted == False:
            self.browser.execute_script("window.scrollTo(0, 2500)")
            time.sleep(4)
            closeButton = self.browser.find_element_by_xpath("//button[@class='Button Modal-closeButton Button--plain']")
            closeButton.click()
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
            
        time.sleep(10)
        answers = self.browser.find_elements_by_xpath("//span[@class='RichText ztext CopyrightRichText-richText' and @itemprop='text']")
        upvotes = self.browser.find_elements_by_xpath("//button[@class='Button VoteButton VoteButton--up']")

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
            
            contentFile.write(re.search("[0-9]+", upvotes[i].get_attribute("aria-label"))[0] + '\n')

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

        if self.crawledQuestionsFile != None:
            self.crawledQuestionsFile.write(str(qId) + '\n')

        if outputInfo == True:
            print("question %s is crawled" % qId)

class zhihuDataAnalyzer:
    def __init__(self):
        pass
    
    def analyzeURLs(self, filePath):
        urlFile = open(filePath, "r")

        urlNum = 0
        httpNum = 0
        for line in urlFile:
            if line[:6] == "ANSWER":
                continue

            url = re.search("href=\"(.*)\"", line)[1]

            if "link.zhihu.com" in url:
                trueUrl = url[len("https://link.zhihu.com/?target="):]

            if trueUrl[:7] == "http%3A":
                httpNum += 1
            
            urlNum += 1

        print("There are totally %s urls, %s of them are http url." % (urlNum, httpNum))

if __name__ == "__main__":
    crawler = zhihuCrawler(crawledQuestionsFilePath="./data/zhihu/crawledQuestions")
    crawler.getAnswersOfQuestionsInFile("./data/zhihu/questions", rawHTML=True, urlParsing=True)
    # cookieString = '_zap=49515c31-8d17-46ad-83ef-72fe146e5b8b; _xsrf=57cfc402-8ad7-479f-980b-126b375e13ca; d_c0="AKDR3iB_CBKPTsNv9KRQFiOO7OY1vsVADg8=|1602587842"; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1602594090|1602587842; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1602582829,1602589334; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1602594089; capsion_ticket="2|1:0|10:1602591831|14:capsion_ticket|44:YjM4YjBiZjI3MzRkNDlmY2I0NDM2ZjU5MWQ1NGUzZGU=|2727d063c8c0508658d72ff123195ea218476ed74945d4a999ced4738b8138bd"; SESSIONID=FRJKJGiKfOum8QOYqoPSObSN21drwAJ1V3n3nItITyL; JOID=VlkRCkleSjAkgr0vH1PpY3GgzyQNHR13ZM7_Q1k-AEBEseplQ6_ms3aBvScZiLmxBOI6Wi334y2glvsHsLo1-VM=; osd=W1ESBU5TQjMrhbAnHFzubnmjwCMAFR54Y8P3QFY5DUhHvu1oS6zptHuJvigehbGyC-U3Ui745CColfQAvbI29lQ=; z_c0="2|1:0|10:1602591842|4:z_c0|92:Mi4xcHV1X0F3QUFBQUFBb05IZUlIOElFaVlBQUFCZ0FsVk5ZdXB5WUFCMGNYUmgwRlk2WnhNcEZYVzE3YXR6NUVxbGtn|0afba122645a51aa553e67a4f07869638952849a434d2481b5e801d9e15fdc5b"; tst=r; tshl='
    # crawler.addCookie(cookieString)
    # crawler.getQuestions(pullDownTimes=500)
    # crawler.getAnswersOfOneQuestion(393259130, urlParsing=True)
    # analyzer = zhihuDataAnalyzer()
    # analyzer.analyzeURLs("data/zhihu/393259130.url")



#!/bin/python3

from selenium import webdriver
import re
import random
import time

class zhihuCrawler:
    def __init__(self):
        self.browser = webdriver.Firefox()
        
    def addCookie(self, cookieString):    
        cookieString = cookieString.replace(' ', '')
        self.browser.get('https://www.zhihu.com')
        for oneCookie in cookieString.split(';'):
            key, value = oneCookie.split('=', 1)
            self.browser.add_cookie({'name': key, 'value': value})

    def getHotQuestions(self, outFile = "hotQuestions"):
        try:
            self.browser.get('https://www.zhihu.com/hot')
        except:
            print("Fail to get https://www.zhihu.com/hot")
            return

        f = open("data/zhihu/%s" % outFile, "r+")
        curQidList = []
        for line in f:
            curQidList.append(int(line))

        questions = self.browser.find_elements_by_xpath("//a[starts-with(@href, 'https://www.zhihu.com/question/') and @title and not(@class)]")
        for oneQuestion in questions:
            qId = re.search("www.zhihu.com/question/([0-9]*)", oneQuestion.get_attribute("href"))[1]
            if qId not in curQidList:
                f.write(qId + '\n')
        f.close()

    def getAnswersOfOneQUestion(self, qId, rawHTML=False, urlParsing=False):
        try:
            self.browser.get("https://www.zhihu.com/question/%s" % qId)
        except:
            print("Fail to get https://www.zhihu.com/hot")
            return

        oldScrollHeight = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            sleepTime = random.randint(1000, 2000) / 1000
            time.sleep(sleepTime)
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight - 500)")
            newScrollHeight = self.browser.execute_script("return document.body.scrollHeight")
            if oldScrollHeight == newScrollHeight:
                break
            else:
                oldScrollHeight = newScrollHeight
        answers = self.browser.find_elements_by_xpath("//span[@class='RichText ztext CopyrightRichText-richText' and @itemprop='text']")

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

        contentFile = open("data/zhihu/%s.content" % qId, "w")
        if urlParsing:
            urlFile = open("data/zhihu/%s.url" % qId, "w")

        for i in range(len(answers)):
            contentFile.write("ANSWER%s:\n" % i)
            
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

if __name__ == "__main__":
    crawler = zhihuCrawler()
    cookieString = '_zap=3a3aee15-b985-4e12-a4c2-f1685fb6418d; _xsrf=i9ppbdW0se7KTrwwudSwbyti855wNgYq; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1601859088,1601896036; d_c0="AICU8iaj_RGPToWuFS_cm9G8sgGylKL9XPo=|1601859088"; capsion_ticket="2|1:0|10:1601859134|14:capsion_ticket|44:ZmY4ZjJlY2EyMGI3NDc0MGJlYzk4MDA2ZmMyNTg1NTE=|5e5e301ae0a367431e3814f2c201630412eeb8b90f0736943d2f2cb6866854c6"; _ga=GA1.2.1285580908.1601859089; _gid=GA1.2.1530831814.1601859089; z_c0="2|1:0|10:1601859134|4:z_c0|92:Mi4xcHV1X0F3QUFBQUFBZ0pUeUpxUDlFU1lBQUFCZ0FsVk5QcnhuWUFEeWpQZVB5N3Nnb1dHcGxZU3FVWXFSMFJkcTJR|c6adcafa0be2d5d7d624aa33916aad48cf3fd7a91a736ede443de11cf9122ba5"; tst=r; KLBRSID=af132c66e9ed2b57686ff5c489976b91|1601896037|1601896034; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1601896036; _gat_gtag_UA_149949619_1=1; SESSIONID=s8sprjV20vj5OhdKiUIVQ3jSwhbLgZuMJXWVyTIk697; JOID=UloVAU3lnrefc6hlEucabjVSCZwDlKTG6wfAMSLT6t-oOMYDW4Bgy8J3qGUUEfqFUOMhQYHJAt8jI850NxAiMWQ=; osd=UlwRA0vlmLOddahjFuUcbjNWC5oDkqDE7QfGNSDV6tmsOsADXYRizcJxrGcSEfyBUuUhR4XLBN8lJ8xyNxYmM2I='
    crawler.addCookie(cookieString)
    crawler.getAnswersOfOneQUestion(393259130, urlParsing=True)
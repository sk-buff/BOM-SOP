import smtplib
from email.mime.text import MIMEText
from email.header import Header

class mailSender():
    def __init__(self, serverUrl, usrname, passwd):
        self.smtpHandler = smtplib.SMTP()
        self.loginStat = True

        try:
            self.smtpHandler.connect(serverUrl, 25)
            self.smtpHandler.login(usrname, passwd)
        except:
            print("Failed to connect or login to the smtp server, please check the input.")
            self.loginStat = False
    
    def sendMail(self, sender, receivers, subject, content, HTMLContent = True):
        if self.loginStat == False:
            print("Didn't login to smtp server")
            return -1

        if HTMLContent == True:
            msg = MIMEText(content, "html", "utf-8")
        else:
            msg = MIMEText(content, "plain", "utf-8")

        msg['From'] = "fluencyl@126.com"
        msg['To'] = ", ".join(receivers)
        msg['Subject'] = Header(subject, 'utf-8')

        try:
            self.smtpHandler.sendmail(sender, receivers, msg.as_string())
        except Exception as e:
            print(e)
            print("Failed to send mail")
            return -1
        
        return 0
    
    def sendHTMLMailFormFile(self, sender, receivers, subject, filePath):
        try:
            f = open(filePath, "r")
        except:
            print("Failed to open file, plz check the file path")
            return -1
        
        content = f.read()
        f.close()

        self.sendMail(sender, receivers, subject, content)

if __name__ == "__main__":
    sender = mailSender("smtp.126.com", "fluencyl@126.com", "OAJFKDISCBDVRGJE")
    sender.sendHTMLMailFormFile("fluencyl@126.com", ["yunvwugua@aliyun.com"], "A problem about html", "mail.htm")
    # sender.sendMail("fluencyl@126.com", ["1005245034@qq.com"], "Ask the slides of poseidon", "Hello, I'm liuchang from tsinghua university, could you please share the slides of poseidon with me?", False)
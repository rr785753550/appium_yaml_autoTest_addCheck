# coding:utf-8
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser


class Email:
    def __init__(self):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p))
        confPath = PATH('../common/emailAddr/emailAddr.txt')
        self.conf = configparser.ConfigParser()
        self.conf.read(confPath, encoding='utf-8')

    def email_sender(self):
        emailSender = {}
        senderName = self.conf.get("emailSender", "name")
        senderPsw = self.conf.get("emailSender", "password")
        emailSender['name'] = senderName
        emailSender['password'] = senderPsw
        # print(emailSender)
        return emailSender

    def email_receiver(self):
        emailReceiver = []
        allKeys = self.conf.options('emailReceiver')
        for key in allKeys:
            temp = self.conf.get('emailReceiver', key)
            emailReceiver.append(temp)
        # print(emailAddr)
        return emailReceiver

    def email_content(self):
        # 邮件主题
        senderName = self.email_sender()['name']
        emailReceiver = self.email_receiver()
        message = MIMEMultipart()
        message['From'] = Header(u"测试" + "<" + senderName + ">", 'utf-8')
        message['To'] = ";".join(emailReceiver)
        message['Subject'] = Header(u"自动化测试报告", 'utf-8')

        # 获取最新的excel报告
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p))
        report_dir = PATH('../results/report/')
        # report_dir = os.path.join(os.getcwd(), 'results/report/')
        report_lists = os.listdir(report_dir)
        report_lists = sorted(report_lists)  # 排序：升序
        if len(report_lists) == 0:
            return None
        print("最新的文件为：" + report_lists[-1])
        report_File = os.path.join(report_dir, report_lists[-1])

        # 邮件内容：
        # emailContent1 = MIMEText("附件为自动化测试报告，请查收", 'plain', 'utf-8')
        emailContent1 = MIMEText(open(report_File, 'rb').read(), 'plain', 'utf-8')
        message.attach(emailContent1)
        # 添加邮件附件1:report.xlsx
        enclosure1 = MIMEText(open(report_File, 'rb').read(), 'base64', 'utf-8')
        enclosure1["Content-Type"] = 'application/octet-stream'
        enclosure1["Content-Disposition"] = 'attachment; filename="report.xlsx"'
        message.attach(enclosure1)

        return message

    def sendreport(self):
        # 发送邮件
        emailSender = self.email_sender()
        senderName = emailSender['name']
        senderPsw = emailSender['password']
        emailReceiver = self.email_receiver()
        try:
            smtp = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
            smtp.login(senderName, senderPsw)
            message = self.email_content()
            if message is None:
                return None
            smtp.sendmail(senderName, emailReceiver, message.as_string())
            smtp.quit()
            print("email has send out!")
        except smtplib.SMTPException:
            print("email send error!")


# if __name__ == '__main__':
    # Email().email_sender()
    # Email().email_sender()
    # Email().email_content()
    # Email().sendreport()

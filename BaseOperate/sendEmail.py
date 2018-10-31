# coding:utf-8
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 定义发件人和收件人
mail_from = "qinyanhui@yunovo.cn"
mail_password = "Qyh2017"
# mail_to = ["1622852733@qq.com", "qinyanhui@yunovo.cn"]
# receiverPath = "F:\\PythonWorkSpace\\autoTest\common\\emailReceiver\\receiverAddr.txt"
receiverPath = os.path.join(os.getcwd(), 'common/emailReceiver/receiverAddr.txt')
fp = open(receiverPath, 'r')
content = fp.readlines()
for i in range(len(content)):
    content[i] = content[i][:len(content[i])-1]
fp.close()
mail_to = content


def email_content():
    # 邮件主题
    message = MIMEMultipart()
    message['From'] = Header(u"测试" + "<" + mail_from + ">", 'utf-8')
    message['To'] = ";".join(mail_to)
    message['Subject'] = Header(u"自动化测试报告", 'utf-8')

    # 获取最新的excel报告
    # report_html_dir = "F:\\PythonWorkSpace\\autoTest\\report\\report"
    report_dir = os.path.join(os.getcwd(), 'results/report/')
    report_lists = os.listdir(report_dir)
    report_lists = sorted(report_lists)  # 排序：升序
    if len(report_lists) == 0:
        return None
    print("最新的文件为：" + report_lists[-1])
    report_File = os.path.join(report_dir, report_lists[-1])

    # # 邮件内容：
    emailContent1 = MIMEText("附件为自动化测试报告，请查收", 'plain', 'utf-8')
    message.attach(emailContent1)

    # 添加邮件附件1:report.xls
    enclosure1 = MIMEText(open(report_File, 'rb').read(), 'base64', 'utf-8')
    enclosure1["Content-Type"] = 'application/octet-stream'
    enclosure1["Content-Disposition"] = 'attachment; filename="report.xlsx"'
    message.attach(enclosure1)

    return message


def sendreport():
    # 发送邮件
    try:
        smtp = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        smtp.login(mail_from, mail_password)
        message = email_content()
        if message is None:
            return None
        smtp.sendmail(mail_from, mail_to, message.as_string())
        smtp.quit()
        print("email has send out!")
    except smtplib.SMTPException:
        print("email send error!")


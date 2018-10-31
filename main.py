# coding:utf-8
import os
import unittest
import HTMLTestRunner
import time
import threading
from BaseOperate.grabLog import kill_logcat
from BaseOperate.appiumServer import *
from BaseOperate.Excel import Report

# report_path = ".\\report\\"
from BaseOperate.sendEmail import sendreport

testcase_path = os.path.join(os.getcwd(), 'testcase/')


def create_suite():  # 创建测试套件
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_settings.py")
    for test_suit in discover:
        for test_case in test_suit:
            suit.addTest(test_case)
    return suit


if __name__ == "__main__":
    start_appium('127.0.0.1', '4723')
    Report().create_workbook()
    Report().create_worksheet1()
    Report().create_worksheet2()
    suit = create_suite()
    unittest.TextTestRunner().run(suit)
    stop_appium(4723)
    kill_logcat()
    Report().closeWorkbook()
    sendreport()  # 发送测试报告
    print('运行完成退出')

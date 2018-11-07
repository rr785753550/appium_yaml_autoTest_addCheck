# coding:utf-8
import threading
import unittest
import datetime
from BaseOperate.grabLog import kill_logcat
from BaseOperate.appiumServer import *
from BaseOperate.Excel1 import Report
from BaseOperate.grabTop import top

# report_path = ".\\report\\"
from BaseOperate.sendEmail import sendreport

testcase_path = os.path.join(os.getcwd(), 'testcase/')


def create_suite():  # 创建测试套件
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_settings1.py")
    for test_suit in discover:
        for test_case in test_suit:
            suit.addTest(test_case)
    return suit

#  设置线程组
threads = []
# 创建新的线程，并添加到线程组中
thread1 = threading.Thread(target=top().start_top)
thread2 = threading.Thread(target=start_appium('127.0.0.1', '4723'))
threads.append(thread1)

if __name__ == "__main__":
    thread1.setDaemon(True)  # 守护线程：主线程一结束，子线程自动结束
    thread2.setDaemon(True)
    for thread in threads:
        thread.start()

    # start_appium('127.0.0.1', '4723')
    Report().create_workbook()
    Report().create_worksheet1()
    Report().create_worksheet2()
    Report().create_worksheet3()
    Report().create_worksheet4()
    suit = create_suite()
    unittest.TextTestRunner().run(suit)
    # 结果所有的服务
    stop_appium(4723)
    kill_logcat()
    top().kill_top()
    # 向excel中写入数据
    Report().worksheet1_write_data()
    Report().worksheet3_write_data()
    Report().worksheet4_write_data()
    Report().closeWorkbook()
    # sendreport()  # 发送测试报告
    # print('运行完成退出')

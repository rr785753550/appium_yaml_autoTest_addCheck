# coding:utf-8
import threading
import unittest
import os
from BaseOperate.grabLog import Logat
from BaseOperate.appiumServer import appium
from BaseOperate.Excel import Report
from BaseOperate.grabTop import top
from BaseOperate.sendEmail import Email


testcase_path = os.path.join(os.getcwd(), 'testcase/')


def create_suite():  # 创建测试套件
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
    for test_suit in discover:
        for test_case in test_suit:
            suit.addTest(test_case)
    return suit

#  设置线程组
threads = []
# 创建新的线程，并添加到线程组中
thread1 = threading.Thread(target=top().start_top())
thread2 = threading.Thread(target=appium().starService('127.0.0.1'))
threads.append(thread1)

if __name__ == "__main__":
    thread1.setDaemon(True)  # 守护线程：主线程一结束，子线程自动结束
    thread2.setDaemon(True)
    for thread in threads:
        thread.start()
    # 创建excel和worksheet
    Report().create_workbook()
    Report().create_worksheet1()
    Report().create_worksheet2()
    Report().create_worksheet3()
    Report().create_worksheet4()
    # 运行测试套件
    suit = create_suite()
    unittest.TextTestRunner().run(suit)
    # 结果所有的服务
    appium().stopService()
    Logat().kill_logcat()
    top().kill_top()
    # 向excel中写入数据
    Report().worksheet1_write_data()
    Report().worksheet3_write_data()
    Report().worksheet4_write_data()
    Report().closeWorkbook()
    Email().sendreport()  # 发送测试报告
    print('运行完成退出')

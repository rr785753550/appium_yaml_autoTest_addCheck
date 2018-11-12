# coding: utf-8
import os
import time


class appium:
    def __init__(self):
        port_num = '4723'
        self.port_num = port_num

    def stopService(self):
        """关闭appium服务"""
        # # 方法一：通过结束所有node的方式结束appium
        # killNode = 'taskkill /f /fi "IMAGENAME eq node.exe" /t'
        # os.popen(killNode)
        # print("结束node进程")

        # 方法二：通过kill appium process的方式
        process = os.popen(f'netstat -ano| findstr {self.port_num}')
        process = process.read().strip()
        # print(process)
        if process != '' and 'LISTENING' in process:
            process = process.split()
            print(process)
            pid = int(process[4])
            os.popen(f'taskkill /F /PID {pid}')
            print("appium进程结束 ")
        else:
            print("未运行appium")
            pass

    def starService(self, ipAdr):
        """启动appium服务"""
        self.stopService()
        appiumLogFolder = os.path.join(os.getcwd(), 'results/appiumLog/')
        now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        appiumFile = 'appium-' + now + '.log'
        appiumLog = os.path.join(appiumLogFolder, appiumFile)
        cmd = f'start /b appium -a {ipAdr} -p {self.port_num} --log ' + appiumLog + ' --local-timezone '
        os.system(cmd)
        time.sleep(5)
        print("appium启动")


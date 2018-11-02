# coding:utf-8
import os
import time
import subprocess


class top:
    def start_top(self):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        topFolder = PATH('../results/top/')
        # topFolder = os.path.join(os.getcwd(), 'results/top/')
        if os.path.exists(topFolder):
            print("top主文件夹已存在，无需创建")
            pass
        else:
            os.mkdir(topFolder)
            print("创建top主文件夹")

        # now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        # topName = now + ".txt"
        topName = "top.txt"
        topFile = os.path.join(topFolder, topName)
        file = open(topFile, "w")
        print("记录top信息")
        topCmd = "adb shell top -m 10 -d 1 -s cpu"
        subprocess.Popen(str(topCmd), shell=True, stdout=file, stderr=subprocess.PIPE)
        file.close()

    def kill_top(self):
        pstopOutput = subprocess.Popen("adb shell ps | findstr top ", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        print(pstopOutput)
        if len(pstopOutput) == 0:
            print("No top process!")
        else:
            for list in pstopOutput:
                list = list.split()     # 以空字符为分隔符，将列表进行分隔
                print(list)
                pid = list[1].decode()
                killPid = "adb shell kill %s " % pid
                os.popen(killPid)
            print("top process was killed!")


# top().start_top()
# time.sleep(10)
# top().kill_top()
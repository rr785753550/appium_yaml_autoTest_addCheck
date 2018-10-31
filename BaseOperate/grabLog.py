# coding: utf-8
import platform
import subprocess
import os
import time


class grabLogat():
    def pc_create_logcatFile(self, tag):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        logcatFolder = PATH('../results/logcat/')
        # logcatFolder = os.path.join(os.getcwd(), 'results/logcat')
        if os.path.exists(logcatFolder):
            # print("logcat主文件夹已存在，无需创建")
            pass
        else:
            os.mkdir(logcatFolder)
            # print("创建logcat主文件夹")
        tag_logcatFolder = os.path.join(logcatFolder, str(tag))
        if os.path.exists(tag_logcatFolder):
            # print("appName的logcat子文件夹已存在，无需创建")
            pass
        else:
            os.mkdir(tag_logcatFolder)
            # print("创建appName的logcat子文件夹")
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        logcatName = now + ".txt"
        logcatFile = os.path.join(tag_logcatFolder, logcatName)
        return logcatFile

    def pc_getTag_logcat(self, tag, logcatFile):
        if platform.system() == "Windows":
            cmd = "adb logcat -v time -s %s " % tag
            # print(cmd)
            openFile = open(logcatFile, 'w', encoding='utf-8')
            subprocess.Popen(cmd, shell=True, stdout=openFile, stderr=subprocess.PIPE)
            openFile.close()

    def phone_create_logcatFile(self, appName):
        os.popen("adb shell mkdir /mnt/sdcard/autoTestLog")
        cmd = 'adb shell mkdir /mnt/sdcard/autoTestLog/%s' % appName
        # print(log_appFolder)
        os.popen(cmd)
        log_appFolder = "/mnt/sdcard/autoTestLog/%s" % appName

        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        # logcatFile = "/mnt/sdcard/autoTestLog/%s/%s.txt" % (appName, now)
        logcatName = now + ".txt"
        # print(logcatName)
        logcatFile = log_appFolder + '/' + logcatName
        return logcatFile, logcatName

    def phone_get_logcat(self, logcatFile):
        # logcatFile = "/mnt/sdcard/autoTestLog/logcat" + str(now) + ".txt"
        if platform.system() == "Windows":
            cmd = "adb logcat -v time -f %s &" % logcatFile
            # print(cmd)
            # os.popen(cmd)
            subprocess.Popen(cmd, shell=True)


def kill_logcat():
    pstopOutput = subprocess.Popen("adb shell ps | findstr logcat ", shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).stdout.readlines()
    # print(pstopOutput)
    if len(pstopOutput) == 0:
        pass
        # print("No logcat process!")
    else:
        for list in pstopOutput:
            list = list.split()  # 以空字符为分隔符，将列表进行分隔
            # print(list)
            pid = list[1].decode()
            killPid = "adb shell kill %s " % pid
            os.popen(killPid)
        # print("logcat process was killed!")


# if __name__ == '__main__':
#     logcatFile = grabLogat().pc_create_logcatFile('YOcSettings')
#     grabLogat().pc_getTag_logcat('YOcSettings', logcatFile)
#     time.sleep(5)
#     kill_logcat()

# coding:utf-8
import os
import subprocess

PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p))
meminfoFolder = PATH('../results/meminfo/')
# meminfoFolder = os.path.join(os.getcwd(), 'results/meminfo/')
if os.path.exists(meminfoFolder):
    print("meminfo主文件夹已存在，无需创建")
    pass
else:
    os.mkdir(meminfoFolder)
    print("创建meminfo主文件夹")
meminfoName = "meminfo"
meminfoTxtFile = os.path.join(meminfoFolder, meminfoName + ".txt")


class meminfo:
    def grab_meminfo(self):
        file = open(meminfoTxtFile, "w")
        print("记录meminfo信息")
        meminfoCmd = "adb shell dumpsys meminfo"
        subprocess.Popen(str(meminfoCmd), shell=True, stdout=file, stderr=subprocess.PIPE)
        file.close()


if __name__ == "__main__":
    meminfo().grab_meminfo()

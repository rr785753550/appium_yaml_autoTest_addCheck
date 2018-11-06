# coding:utf-8
import os
import time
import subprocess
import xlsxwriter

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

topName = "top"
topTxtFile = os.path.join(topFolder, topName + ".txt")


class top:
    def start_top(self):
        file = open(topTxtFile, "w")
        print("记录top信息")
        topCmd = "adb shell top -m 10 -d 1 -s cpu"
        subprocess.Popen(str(topCmd), shell=True, stdout=file, stderr=subprocess.PIPE)
        file.close()

    def kill_top(self):
        pstopOutput = subprocess.Popen("adb shell ps | findstr top ", shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE).stdout.readlines()
        print(pstopOutput)
        if len(pstopOutput) == 0:
            print("No top process!")
        else:
            for list in pstopOutput:
                list = list.split()  # 以空字符为分隔符，将列表进行分隔
                print(list)
                pid = list[1].decode()
                killPid = "adb shell kill %s " % pid
                os.popen(killPid)
            print("top process was killed!")

    def read_topText(self):
        """按行读取top.txt文件内容"""
        lines = open(topTxtFile, 'r').readlines()
        # print(lines)
        arrays = []
        for line in lines:
            if not line.startswith(('\n', 'User')):     # 去除字符串以元组中任意一个元素开头的
                arrays.append(line.split())
        # print(arrays)
        cols_name = arrays[0]          # 提取top信息中每一列的名称标题
        # print(cols_name)
        apps_lines = []             # 提取app的top信息
        for line in arrays:
            if cols_name != line:
                apps_lines.append(line)
        # print(apps_lines)
        top = []
        top.append(cols_name)
        top.extend(apps_lines)
        print(top)
        return top

    def top_list_xls(self, workbook):
        topData = self.read_topText()
        worksheet = workbook.get_worksheet_by_name("top")
        i = 0
        for data in topData:
            for j in range(len(data)):
                worksheet.write(i, j, data[j])
            i += 1


# if __name__ == "__main__":
#     # top().start_top()
#     # time.sleep(10)
#     # top().kill_top()
#     # 打开excel
#     # workbook = xlwt.Workbook(encoding='utf-8')
#     # sheet1 = workbook.add_sheet(u"top")
#     topExcelFile = os.path.join(topFolder, topName + ".xlsx")
#     workbook = xlsxwriter.Workbook(topExcelFile)
#     sheet1 = workbook.add_worksheet("top")
#     # top().top_list_xls(workbook)
#     workbook.close()

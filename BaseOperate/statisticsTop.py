# coding: utf-8
import xlsxwriter
import os, subprocess
import time
import xlrd
from matplotlib import pyplot

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
topExcelFile = os.path.join(topFolder, topName + ".xlsx")


class top:
    workbook = xlsxwriter.Workbook("")

    def grabTop(self):
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

    def top_list_xls(self):
        top = self.read_topText()
        # 打开excel
        # workbook = xlwt.Workbook(encoding='utf-8')
        # sheet1 = workbook.add_sheet(u"top")
        top.workbook = xlsxwriter.Workbook(topExcelFile)
        sheet1 = top.workbook.add_worksheet("top")
        i = 0
        for data in top:
            for j in range(len(data)):
                sheet1.write(i, j, data[j])
            i += 1
        # workbook.save(topExcelFile)
        top.workbook.close()

    def top_list_lineChart(self):
        data = self.read_topText()[1:]
        print(data)
        name_list = []
        for i in range(len(data)):
            name_list.append(data[i][9])
        # print(name_list)
        name_only_list = list(set(name_list))   # 筛选列表中内容不重复的为新列表
        name_only_list.sort(key=name_list.index)
        # print(name_only_list)
        cpuDict = {}
        for i in range(len(name_only_list)):
            temp = []
            for j in range(len(data)):
                if name_only_list[i] == data[j][9]:
                    temp.append(data[j][2])
            # print(temp)
            cpuDict[name_only_list[i]] = temp
        print(cpuDict)      # 分隔以name分隔出所抓取的cpu数据
        for key in cpuDict.keys():
            key_values = cpuDict.get(key)
            # print(key)
            # print(key_values)
            y_values = []
            for i in range(len(key_values)):
                tmp = int(key_values[i].split("%")[0])
                y_values.append(tmp)
            # print(y_values)
            x_values = []
            for i in range(len(key_values)):
                x_values.append(i+1)
            # print(x_values)
            pyplot.plot(x_values, y_values, linewidth=1)
            pyplot.title(key)
            pyplot.xlabel("number")
            pyplot.ylabel('CPU%')
            pyplot.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])     # y轴刻度
            # pyplot.show()
            pyplot.savefig("test.png")




if __name__ == "__main__":
    # top().grabTop()
    # time.sleep(10)
    # top().kill_top()
    # top().top_list_xls()
    top().top_list_lineChart()


# coding: utf-8
from BaseOperate.get_testcaseyaml_info import getyamlInfo
import subprocess, os, time
from BaseOperate.grabLog import grabLogat, kill_logcat


# 针对把log保存的pc端时读取方式
class AnalysisLog:
    # def pull_logFile(self, phone_logFile, phone_logName, appName):   # 若分析存在手机端的log则先把log导出再分析
    #
    #     PATH = lambda p: os.path.abspath(
    #         os.path.join(os.path.dirname(__file__), p)
    #     )
    #     pc_logcatFolder = PATH('../results/logcat')
    #     pc_applog_Folder = os.path.join(pc_logcatFolder, appName)
    #     if os.path.exists(pc_applog_Folder):
    #         pass
    #     else:
    #         os.mkdir(pc_applog_Folder)
    #     print(pc_applog_Folder)
    #
    #     cmd = "adb pull %s %s" % (phone_logFile, pc_applog_Folder)
    #     print(cmd)
    #     subprocess.Popen(cmd, shell=True)
    #     time.sleep(3)
    #     pc_logcatFile = pc_applog_Folder + '/' + phone_logName
    #     return pc_logcatFile

    def get_logData(self, logFile):
        textData = open(logFile, 'r', encoding='utf-8')
        line = textData.readlines()
        textData.close()
        # print(line)
        return line

    def get_check_content_List(self, yamlpath):
        checkKeys = getyamlInfo(yamlpath).get_checkDate()
        check_content_list = []
        for key in checkKeys:
            check_content = getyamlInfo(yamlpath).get_check_content(key)
            check_content_list.append(check_content)    # 添加check中的每个key中的check_content值
        # print(check_content_list)
        check_content_list2 = list(set(check_content_list))        # 去除列表中内容相同的元素
        check_content_list2.sort(key=check_content_list.index)     # 对列表按原有列表顺序进行排序
        # print(check_content_list2)
        return check_content_list2

    def get_results_list(self, logFile, yamlpath):
        resultsList = []
        logData = self.get_logData(logFile)
        # print(logData)
        check_contentList = self.get_check_content_List(yamlpath)
        # print(check_contentList)
        for i in range(len(check_contentList)):
            for j in range(len(logData)):
                if check_contentList[i] in logData[j]:
                    resultsList.append(logData[j])     # 提取line中所有满足check_content_list要求的内容
        resultsList.sort()
        # print(resultsList)
        return resultsList

    def get_actualValue_list(self, logFile, yamlpath):
        resultsList = self.get_results_list(logFile, yamlpath)
        actualValue_list = []
        for item in resultsList:
            tmp = item.split(" ")  # 转化为列表
            actualValue = tmp[-1][0: -1]
            if "," in actualValue:      # 防止打印的log数据未用空格分开，而是用，或：分隔
                m = actualValue.split(",")
                actualValue = m[-1]
            elif ":" in actualValue:
                m = actualValue.split(":")
                actualValue = m[-1]
            # print(actualValue)
            actualValue_list.append(actualValue)
        # print(actualValue_list)
        return actualValue_list


        # resultsList_1 = []      # 从check_content的位置截取resultsList内容
        # for item in resultsList:
        #     for key in checkKeys:
        #         check_content = getyamlInfo(yamlpath).get_check_content(key)
        #         if check_content in item:
        #             startPoint = item.find(check_content)
        #             # print(startPoint)
        #             tmp = item[startPoint: -1]
        #             print(tmp)
        #             resultsList_1.append(tmp)
        # print(resultsList_1)
        # 筛选出对应的check_content为ke，结果为value（这种方法不行，若key值相同时，则仅会保留一个，无法全部保留）
        # resultDict = {}
        # for item in resultsList_1:
        #     if "," in item:
        #         tmp = item.split(",")
        #         print(tmp)
        #         resultDict[tmp[0]] = tmp[-1]
        #     elif " : " in item:
        #         tmp = item.split(" : ")
        #         print(tmp)
        #         resultDict[tmp[0]] = tmp[-1]
        #     elif " = " in item:
        #         tmp = item.split(" = ")
        #         print(tmp)
        #         resultDict[tmp[0]] = tmp[-1]
        # print(resultDict)






        # for temp in resultsList:   # 对resulteList进行分隔获得所需的value
        #     # print(list1)
        #     split_temp = temp.split("): ")
        #     print(split_temp)
        #     temp1 = split_temp[1]
        #     print(temp1)
        #     split_temp1 = temp1.split(" ")
        #     print(split_temp1)
        #     temp2 = split_temp1[-1][0: -1]
        #     print(temp2)


# if __name__ == "__main__":
    # logcatFile, logcatName = grabLogat().phone_create_logcatFile('settings')
    # grabLogat().phone_get_logcat(logcatFile)
    # time.sleep(5)
    # pc_logcatFile = AnalysisLog().pull_logFile(phone_logFile=logcatFile, phone_logName=logcatName, appName='settings')
    # time.sleep(10)
    # line = AnalysisLog().get_logData(pc_logcatFile)
    # print(line)
    # kill_logcat()
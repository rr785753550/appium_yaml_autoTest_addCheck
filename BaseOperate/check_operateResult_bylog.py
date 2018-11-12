# coding: utf-8
from BaseOperate.get_testcaseyaml_info import getyamlInfo


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
        if check_content_list2 == [None]:
            return None
        return check_content_list2

    def get_results_list(self, logFile, yamlpath):
        resultsList = []
        logData = self.get_logData(logFile)
        # print(logData)
        check_contentList = self.get_check_content_List(yamlpath)
        if check_contentList is None:
            return None
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
        if resultsList is None:
            return None
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


# if __name__ == "__main__":
#     # logcatFile, logcatName = grabLogat().phone_create_logcatFile('settings')
#     # grabLogat().phone_get_logcat(logcatFile)
#     # time.sleep(5)
#     # pc_logcatFile = AnalysisLog().pull_logFile(phone_logFile=logcatFile, phone_logName=logcatName, appName='settings')
#     # time.sleep(10)
#     # line = AnalysisLog().get_logData(pc_logcatFile)
#     # print(line)
#     # grabLogat().kill_logcat()
#     yamlpath = "F:\\PythonWorkSpace\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\settings\\02_hotspot.yaml"
#     print(AnalysisLog().get_check_content_List(yamlpath))
#     logcatFile = "F:\\PythonWorkSpace\\appium_yaml_autoTest_addCheck\\results\\logcat\\YOcSettings\\20181031162014.txt"
#     print(AnalysisLog().get_results_list(logcatFile, yamlpath))
#     print(AnalysisLog().get_actualValue_list(logcatFile, yamlpath))

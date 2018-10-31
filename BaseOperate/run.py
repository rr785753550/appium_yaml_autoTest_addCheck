# coding: utf-8
from BaseOperate.get_testcaseyaml_info import getyamlInfo
from BaseOperate.elementOperate import Operate
from BaseOperate.grabLog import *
from BaseOperate.check_operateResult_bylog import AnalysisLog
import time


class run_testcaseYaml:
    def __init__(self, driver, yamlFile):
        self.driver = driver
        self.yamlFile = yamlFile
        # self.tag = logcatTag

    def run_testcase(self, tag):
        kill_logcat()
        time.sleep(2)
        # 执行logcat
        # logcatFile = grabLogat().phone_create_logcatFile(appName)
        # grabLogat().phone_get_logcat(logcatFile)
        logcatFile = grabLogat().pc_create_logcatFile(tag)
        grabLogat().pc_getTag_logcat(tag, logcatFile)
        # 执行用例
        testcaseList = getyamlInfo(self.yamlFile).get_testcaseData()  # 将某个yaml文件testcase信息生成为列表
        # print(testcaseList)
        for step in testcaseList.keys():
            Operate(self.driver, self.yamlFile).operate_element(step)

        # get期待的结果列表
        checkList = getyamlInfo(self.yamlFile).get_checkDate()
        # print(checkList)
        expectValue_list = []
        for check in checkList.keys():
            expect_value = getyamlInfo(self.yamlFile).get_expect_value(check)
            expectValue_list.append(expect_value)
        print("expectValue_list:", expectValue_list)

        pass_output = getyamlInfo(self.yamlFile).get_pass_output()
        fail_output = getyamlInfo(self.yamlFile).get_fail_output()

        actualValue_list = ''
        resultOutput = ''
        testConclusion = ''
        for i in range(3):
            # get实际测试结果
            actualValue_list = AnalysisLog().get_actualValue_list(logcatFile, self.yamlFile)
            print("actualValue_list:", actualValue_list)
            if expectValue_list == actualValue_list:
                resultOutput = pass_output
                testConclusion = 'pass'
                break
            else:
                time.sleep(1)
        if expectValue_list != actualValue_list:
            resultOutput = fail_output
            testConclusion = 'fail'
        return actualValue_list, resultOutput, testConclusion




# if __name__ == "__main__":
#     tag = "YOcSettings"
#     from BaseOperate.getDriver import mdriver
#     driver = mdriver('settings')
#     yamlFile = "F:\\PythonWorkSpace\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\settings\\01_wifi.yaml"
#     output = run_testcaseYaml(driver, yamlFile).run_testcase(tag)
#     print(output)

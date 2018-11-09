# coding: utf-8
from BaseOperate.get_testcaseyaml_info import getyamlInfo
from BaseOperate.elementOperate import Operate
from BaseOperate.grabLog import *
from BaseOperate.check_operateResult_bylog import AnalysisLog
import time


class run_testcaseYaml:
    passNum = 0
    failNum = 0
    logcatFile = grabLogat().pc_create_logcatFile()

    def __init__(self, yamlFile):
        self.yamlFile = yamlFile

    def run_testcase(self, driver, tag):
        kill_logcat()
        time.sleep(2)
        # 运行脚本之前先执行logcat
        # logcatFile = grabLogat().phone_create_logcatFile(appName)
        # grabLogat().phone_get_logcat(logcatFile)
        grabLogat().pc_getTag_logcat(tag, self.logcatFile)
        time.sleep(3)
        # 执行用例
        testcaseList = getyamlInfo(self.yamlFile).get_testcaseData()  # 将某个yaml文件testcase信息生成为列表
        # print(testcaseList)
        for step in testcaseList.keys():
            Operate(driver, self.yamlFile).operate_element(step)

    def get_run_results(self):
        # get期待的结果列表
        checkList = getyamlInfo(self.yamlFile).get_checkDate()
        print(checkList)
        expectValue_list = []
        for check in checkList.keys():
            expect_value = getyamlInfo(self.yamlFile).get_expect_value(check)
            if expect_value is None:
                expectValue_list = None
                break
            expectValue_list.append(expect_value)
        print("expectValue_list:", expectValue_list)

        pass_output = getyamlInfo(self.yamlFile).get_pass_output()
        fail_output = getyamlInfo(self.yamlFile).get_fail_output()

        actualValue_list = []
        resultOutput = ''
        testConclusion = ''
        for i in range(3):
            # get实际测试结果
            actualValue_list = AnalysisLog().get_actualValue_list(self.logcatFile, self.yamlFile)
            print("actualValue_list:", actualValue_list)
            if actualValue_list is None or expectValue_list is None:    # 以防yaml中未传入任何数据无法判断
                time.sleep(2)
                resultOutput = "期待结果或实际结果列表为空，无法自动判断"
                testConclusion = "NA"
            elif expectValue_list == actualValue_list and (actualValue_list is not None) and (expectValue_list is not None):
                kill_logcat()
                time.sleep(2)
                os.remove(self.logcatFile)  # 如果相同，则删除logcat文件
                resultOutput = pass_output
                testConclusion = 'pass'
                run_testcaseYaml.passNum += 1
                break
            else:
                time.sleep(1)
        if expectValue_list != actualValue_list:
            kill_logcat()
            resultOutput = fail_output
            testConclusion = 'fail'
            run_testcaseYaml.failNum += 1
        result_tuple = actualValue_list, resultOutput, testConclusion
        # return actualValue_list, resultOutput, testConclusion
        return result_tuple


if __name__ == "__main__":
    tag = "YOcSettings"
    from BaseOperate.getDriver import mdriver
    driver = mdriver('settings')
    yamlFile = "F:\\PythonWorkSpace\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\settings\\01_wifi.yaml"
    try:
        run_testcaseYaml(yamlFile).run_testcase(driver, tag)
    finally:
        output = run_testcaseYaml(yamlFile).get_run_results()
        print(output)
        print(output[0])


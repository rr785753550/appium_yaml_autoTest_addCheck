# coding: utf-8
"""
        读取yaml信息并执行
        element_info：定位元素信息
        find_type：属性id、xpath、text、class
        operate_type: click、sendkeys
        send_content：send_keys
        index：ids时用
"""
from BaseOperate.elementMethod import Element
from BaseOperate.check_operateResult_bylog import *
from time import sleep


class Operate:
    def __init__(self, driver, yamlPath):
        self.driver = driver
        self.yamlPath = yamlPath
        self.yaml = getyamlInfo(self.yamlPath)
        self.findele = Element(driver)

    def operate_element(self, key):
        element_info = self.yaml.get_element_info(key)
        element_type = self.yaml.get_element_type(key)
        element_operate = self.yaml.get_element_operate(key)
        operate_times = self.yaml.get_operate_times(key)
        sleep_time = self.yaml.get_sleep_time(key)

        if element_operate == "click":  # 对元素执行点击操作
            self.driver.implicitly_wait(3)
            if element_type == "id":
                for j in range(operate_times):
                    self.findele.find_id(element_info).click()
                    sleep(sleep_time)
            elif element_type == "text":
                for j in range(operate_times):
                    self.findele.find_text(element_info).click()
                    sleep(sleep_time)
            elif element_type == "class":
                for j in range(operate_times):
                    self.findele.find_class(element_info).click()
                    sleep(sleep_time)
            elif element_type == "xpath":
                for j in range(operate_times):
                    self.findele.find_xpath(element_info).click()
                    sleep(sleep_time)

        elif element_operate == "tap":
            self.driver.implicitly_wait(3)
            for j in range(operate_times):
                self.findele.find_position(element_info)
                sleep(sleep_time)

        elif element_operate == "back":
            self.driver.implicitly_wait(3)
            for j in range(operate_times):
                self.driver.press_keycode(4)
                sleep(sleep_time)

        elif element_operate == "swipe_up":
            self.driver.implicitly_wait(3)
            if element_type == "id":
                element = self.findele.find_id(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)
            elif element_type == "text":
                element = self.findele.find_text(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)
            elif element_type == "class":
                element = self.findele.find_class(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)
            elif element_type == "xpath":
                element = self.findele.find_xpath(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)

        elif element_operate == "swipe_down":
            self.driver.implicitly_wait(3)
            if element_type == "id":
                element = self.findele.find_id(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)
            elif element_type == "text":
                element = self.findele.find_text(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)
            elif element_type == "class":
                element = self.findele.find_class(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)
            elif element_type == "xpath":
                element = self.findele.find_xpath(element_info)
                for j in range(operate_times):
                    self.findele.swipeUp_element(element)
                    sleep(sleep_time)

        elif element_operate == "swipe_left":
            self.driver.implicitly_wait(3)
            if element_type == "id":
                element = self.findele.find_id(element_info)
                for j in range(operate_times):
                    self.findele.swipeLeft_element(element)
                    sleep(sleep_time)
            elif element_type == "text":
                element = self.findele.find_text(element_info)
                for j in range(operate_times):
                    self.findele.swipeLeft_element(element)
                    sleep(sleep_time)
            elif element_type == "class":
                element = self.findele.find_class(element_info)
                for j in range(operate_times):
                    self.findele.swipeLeft_element(element)
                    sleep(sleep_time)
            elif element_type == "xpath":
                element = self.findele.find_xpath(element_info)
                for j in range(operate_times):
                    self.findele.swipeLeft_element(element)
                    sleep(sleep_time)

        elif element_operate == "swipe_right":
            self.driver.implicitly_wait(3)
            if element_type == "id":
                element = self.findele.find_id(element_info)
                for j in range(operate_times):
                    self.findele.swipeRight_element(element)
                    sleep(sleep_time)
            elif element_type == "text":
                element = self.findele.find_text(element_info)
                for j in range(operate_times):
                    self.findele.swipeRight_element(element)
                    sleep(sleep_time)
            elif element_type == "class":
                element = self.findele.find_class(element_info)
                for j in range(operate_times):
                    self.findele.swipeRight_element(element)
                    sleep(sleep_time)
            elif element_type == "xpath":
                element = self.findele.find_xpath(element_info)
                for j in range(operate_times):
                    self.findele.swipeRight_element(element)
                    sleep(sleep_time)

        elif element_operate == "send_keys":
            self.driver.implicitly_wait(3)
            sendContent = self.yaml.get_send_content(key)
            if element_type == "id":
                element = self.findele.find_id(element_info)
                element.send_keys(sendContent)
            elif element_type == "class":
                element = self.findele.find_class(element_info)
                element.send_keys(sendContent)
            elif element_type == "text":
                element = self.findele.find_text(element_info)
                element.send_keys(sendContent)
            elif element_type == "xpath":
                element = self.findele.find_xpath(element_info)
                element.send_keys(sendContent)
            sleep(sleep_time)

        elif element_operate == "seekBar":
            self.driver.implicitly_wait(3)
            if element_type == "id":
                element = self.findele.find_id(element_info)
                self.findele.seekBar_tapLocation(element)
            elif element_type == "class":
                element = self.findele.find_class(element_info)
                self.findele.seekBar_tapLocation(element)
            elif element_type == "text":
                element = self.findele.find_text(element_info)
                self.findele.seekBar_tapLocation(element)
            elif element_type == "xpath":
                element = self.findele.find_xpath(element_info)
                self.findele.seekBar_tapLocation(element)
            sleep(sleep_time)

    # def check_operate(self, key, logcatFile):
    #     get_check_method = self.yaml.get_check_method(key)
    #     get_check_content = self.yaml.get_check_content(key)
    #     if get_check_method == "check_logcatContent":
    #         self.driver.implicitly_wait(3)
    #         actualValue = checkResult().get_results_list(logcatFile, self.yamlpath)
    #     elif get_check_method == "check_sysContent":
    #         self.driver.implicitly_wait(3)
    #         actualValue = checkOperateResult(get_check_content).check_logcatContent(logcatFile)
    #     elif get_check_method == "elementExist":
    #         self.driver.implicitly_wait(3)
    #         actualValue = checkOperateResult(get_check_content).check_elementExist(self.driver)
    #     return actualValue


# if __name__ == "__main__":
#     from BaseOperate.getDriver import mdriver
#     driver = mdriver("xiset")
#     sleep(2)
#     yamlpath = "E:\\PycharmProjects\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\xiSettings\settings1.yaml"
#     logcatFile = "/mnt/sdcard/YOcSettings.txt"
#     Operate(driver, yamlpath).operate_element('step1')
#     Operate(driver, yamlpath).operate_element('step2')
#     logcatFile = "/mnt/sdcard/autoTest/logcat.txt"
#     Operate(driver, yamlpath).check_operate('result1', logcatFile)


# coding: utf-8
"""读取yaml文件"""
""""进入应用主界面，主界面中每个功能代表一个testcase；
    每个testcase中依次执行操作；
    get_yamlData:获取yaml中所有的数据；
    get_testcaseDate：获取某个testcase的value值；
    get_testcase_len：获取某个testcase中的操作需操作次数
    get_element_info/type/operate：获取某个testcase中某个操作的相关信息"""
import yaml


class getyamlInfo:
    def __init__(self, path):
       self.path = path

    def get_yamlData(self):
        # 获取yaml文件中数据
        try:
            file = open(self.path, 'r', encoding='utf-8')
            data = yaml.load(file)
            file.close()
            # print(data)
            return data
        except:
            # print("未找到yaml文件")
            pass

    def get_title(self):
        # 获取get_title
        title = self.get_yamlData()['testinfo']['title']
        # print(get_title)
        return title

    def get_condition(self):
        condition = self.get_yamlData()['testinfo']['condition']
        return condition

    def get_testcaseData(self):
        # 获取testcase中的操作信息
        testcase_data = self.get_yamlData()['testcase']
        # print(testcase_data)
        return testcase_data

    def get_element_info(self, key):
        data = self.get_yamlData()
        element_info = data['testcase'][key]['element_info']
        # print(element_info)
        return element_info

    def get_element_type(self, key):
        data = self.get_yamlData()
        element_type = data['testcase'][key]['element_type']
        # print(element_type)
        return element_type

    def get_element_operate(self, key):
        data = self.get_yamlData()
        element_operate = data['testcase'][key]['element_operate']
        # print(element_operate)
        return element_operate

    def get_operate_times(self, key):
        data = self.get_yamlData()
        operate_times = data['testcase'][key]['operate_times']
        return operate_times

    def get_sleep_time(self, key):
        data = self.get_yamlData()
        sleep_time = data['testcase'][key]['sleep_time']
        return sleep_time

    def get_operate_details(self, key):
        data = self.get_yamlData()
        operate_details = data['testcase'][key]['operate_details']
        # print(operate_details)
        return operate_details

    def get_send_content(self, key):
        """控件send_keys内容"""
        data = self.get_yamlData()
        if self.get_element_operate(key) == "send_keys":
            send_content = data['testcase'][key]['send_content']
            return send_content
        else:
            pass

    def get_checkDate(self):
        # 获取check中的操作信息
        check_data = self.get_yamlData()['check']
        return check_data

    def get_check_content(self, key):
        data = self.get_yamlData()
        check_content = data['check'][key]['check_content']
        return check_content

    def get_check_method(self, key):
        data = self.get_yamlData()
        check_method = data['check'][key]['check_method']
        return check_method

    def get_expect_value(self, key):
        data = self.get_yamlData()
        expect_value = data['check'][key]['expect_value']
        return expect_value

    def get_pass_output(self):
        data = self.get_yamlData()
        pass_output = data['output']['pass_output']
        return pass_output

    def get_fail_output(self):
        data = self.get_yamlData()
        fail_output = data['output']['fail_output']
        return fail_output


# if __name__ == "__main__":
#     yamlpath = "F:\\PythonWorkSpace\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\settings\\02_hotspot.yaml"
#     print(getyamlInfo(yamlpath).get_yamlData())
#     print(getyamlInfo(yamlpath).get_testcaseData())
#     print(getyamlInfo(yamlpath).get_checkDate())
#     testcaseKeys = getyamlInfo(yamlpath).get_testcaseData().keys()
#     for key in testcaseKeys:
#         element_info = getyamlInfo(yamlpath).get_element_info(key)
#         element_type = getyamlInfo(yamlpath).get_element_type(key)
#         element_operate = getyamlInfo(yamlpath).get_element_operate(key)
#         operate_times = getyamlInfo(yamlpath).get_operate_times(key)
#         sleep_time = getyamlInfo(yamlpath).get_sleep_time(key)
#         operate_details = getyamlInfo(yamlpath).get_operate_details(key)
#         send_content = getyamlInfo(yamlpath).get_send_content(key)
#         print(element_info, element_type, element_operate, operate_times, sleep_time, operate_details, send_content)
#     checkKeys = getyamlInfo(yamlpath).get_checkDate().keys()
#     for key in checkKeys:
#         check_content = getyamlInfo(yamlpath).get_check_content(key)
#         expect_value = getyamlInfo(yamlpath).get_expect_value(key)
#         print(check_content, expect_value)


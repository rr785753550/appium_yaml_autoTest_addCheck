# coding: utf-8
from BaseOperate.get_testcaseyaml_info import getyamlInfo


class writeTestcase:
    initRow = 2

    def set_Workbookformat_content(self, workbook):
        # 设置单元格格式: 表格中其它内容格式
        workbook_content_format = workbook.add_format(
            {
                'align': 'center',  # 水平居中
                'font_size': 10,
                'border': 1,
                'valign': 'vcenter',  # 垂直居中
                'text_wrap': 1  # 自动换行
            })
        return workbook_content_format

    def write_case_title(self, yamlFile):
         title = getyamlInfo(yamlFile).get_title()
         # print(title)
         # print(data['caseTitle']['value'])
         return title

    def write_case_condition(self, yamlFile):
        condition = getyamlInfo(yamlFile).get_condition()
        # print(data['caseCondition']['value'])
        return condition

    def write_case_step(self, yamlFile):
        # 传入测试步骤
        step = ""
        i = 1
        caseLength = len(getyamlInfo(yamlFile).get_testcaseData())
        if i <= caseLength:
            for key in getyamlInfo(yamlFile).get_testcaseData().keys():
                step += str(i) + '.' + getyamlInfo(yamlFile).get_operate_details(key) + '\n'
                i += 1
        # data['caseSteps']['value'] = step
        return step

    def write_case_check(self, yamlFile):
        # 传入测试检查点
        check = ""
        i = 1
        caseLength = len(getyamlInfo(yamlFile).get_checkDate())
        if i <= caseLength:
            for key in getyamlInfo(yamlFile).get_checkDate().keys():
                if getyamlInfo(yamlFile).get_check_content(key) is not None:
                    check += str(i) + '.' + getyamlInfo(yamlFile).get_check_content(key) + '\n'
                else:
                    check = '空'
                i += 1
        # data['caseCheck']['value'] = check
        return check

    def write_case_expectResult(self, yamlFile):
        # 传入测试期待结果
        expectResult = ""
        i = 1
        caseLength = len(getyamlInfo(yamlFile).get_checkDate())
        if i <= caseLength:
            for key in getyamlInfo(yamlFile).get_checkDate().keys():
                if getyamlInfo(yamlFile).get_expect_value(key) is not None:
                    expectResult += str(i) + '.' + getyamlInfo(yamlFile).get_expect_value(key) + '\n'
                else:
                    expectResult = "空"
                i += 1
        # data['expectResult']['value'] = expectResult
        return expectResult

    def write_case_actualResult(self, result_tuple):
        actualResult_List, resultOutput, testConclusion = result_tuple
        # 传入实际结果
        actualResult = ""
        if actualResult_List is None:
            actualResult = "空"
        else:
            for i in range(len(actualResult_List)):
                actualResult += str(i + 1) + '.' + actualResult_List[i] + '\n'
        output_tuple = actualResult, resultOutput, testConclusion
        print(output_tuple)
        return output_tuple

    def worksheet2_write_data(self, workbook, yamlFile, result_tuple):
        # actualResult_List, resultOutput, testConclusion = result_tuple
        writeTestcase.initRow += 1
        row = writeTestcase.initRow
        content_formate = self.set_Workbookformat_content(workbook)
        worksheet2 = workbook.get_worksheet_by_name("测试详情")
        # 所需填写的结果
        data = {'caseTitle': {'position': 'A' + str(row), 'value': ''},
                'caseCondition': {'position': 'B' + str(row), 'value': ''},
                'caseSteps': {'position': 'C' + str(row), 'value': ''},
                'caseCheck': {'position': 'D' + str(row), 'value': ''},
                'expectResult': {'position': 'E' + str(row), 'value': ''},
                'actualResult': {'position': 'F' + str(row), 'value': ''},
                'resultOutput': {'position': 'G' + str(row), 'value': ''},
                'testConclusion': {'position': 'H' + str(row), 'value': ''},
                'screenshot': {'position': 'I' + str(row), 'value': ''}}
        data['caseTitle']['value'] = self.write_case_title(yamlFile)
        data['caseCondition']['value'] = self.write_case_condition(yamlFile)
        data['caseSteps']['value'] = self.write_case_step(yamlFile)
        data['caseCheck']['value'] = self.write_case_check(yamlFile)
        data['expectResult']['value'] = self.write_case_expectResult(yamlFile)
        output_tuple = self.write_case_actualResult(result_tuple)
        # actualResult, resultOutput, testConclusion = output_tuple
        data['actualResult']['value'] = output_tuple[0]
        data['resultOutput']['value'] = output_tuple[1]
        data['testConclusion']['value'] = output_tuple[2]
        for key in data.keys():
            location = data[key]['position']
            value = data[key]['value']
            worksheet2.write(location, value, content_formate)


# if __name__ == '__main__':
#     import xlsxwriter
#     workbook = xlsxwriter.Workbook("testcase.xlsx")
#     writeTestcase().create_worksheet2(workbook)
#     yamlFile = "F:\\PythonWorkSpace\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\settings\\01_wifi.yaml"
#     result_tuple = 1, 2, 3
#     writeTestcase().worksheet2_write_data(workbook, yamlFile)
#     workbook.close()

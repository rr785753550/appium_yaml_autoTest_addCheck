# coding: utf-8
from BaseOperate.get_testcaseyaml_info import getyamlInfo
import xlsxwriter


class writeTestcase:
    initRow = 2


    def set_Workbookformat_subject(self, workbook):
        # 设置单元格格式: 表格中主题格式
        workbook_subject_format = workbook.add_format(
            {
                'bold': True,  # 字体加粗
                'border': 6,  # 单元格边框宽度
                'align': 'center',  # 水平居中
                'font_size': 18,
                'valign': 'vcenter',  # 垂直居中
                'fg_color': '#D7E4BC',  # 填充颜色
                'text_wrap': 1  # 自动换行
            })
        return workbook_subject_format

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

    def create_worksheet2(self, workbook):
        subject_formate = self.set_Workbookformat_subject(workbook)
        content_formate = self.set_Workbookformat_content(workbook)
        worksheet2 = workbook.add_worksheet("测试详情")  # 创建sheet表单对象
        # 设置列和行的宽度高度
        worksheet2.set_column('A:I', 20)
        for i in range(100):
            worksheet2.set_row(i, 40)
        # 设置第一行总标题
        worksheet2.merge_range('A1:I1', u'测试详情', subject_formate)
        # 所需显示的内容标题
        title = ['用例标题', '前置条件', '操作步骤', '检查点', '预期结果', '实际结果', '测试结果输出', '测试结论', '截图']
        worksheet2.write('A2', title[0], content_formate)
        worksheet2.write('B2', title[1], content_formate)
        worksheet2.write('C2', title[2], content_formate)
        worksheet2.write('D2', title[3], content_formate)
        worksheet2.write('E2', title[4], content_formate)
        worksheet2.write('F2', title[5], content_formate)
        worksheet2.write('G2', title[6], content_formate)
        worksheet2.write('H2', title[7], content_formate)
        worksheet2.write('I2', title[8], content_formate)

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

    def worksheet2_write_data1(self, workbook, yamlFile):
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
        data['caseTitle']['value'] = self.write_case_step(yamlFile)
        data['caseCondition']['value'] = self.write_case_condition(yamlFile)
        data['caseSteps']['value'] = self.write_case_step(yamlFile)
        data['caseCheck']['value'] = self.write_case_check(yamlFile)
        data['expectResult']['value'] = self.write_case_expectResult(yamlFile)
        # actualResult = ""
        # resultOutput = ""
        # testConclusion = ""
        # data['actualResult']['value'] = actualResult
        # data['resultOutput']['value'] = resultOutput
        # data['testConclusion']['value'] = testConclusion
        for key in data.keys():
            location = data[key]['position']
            value = data[key]['value']
            worksheet2.write(location, value, content_formate)


# if __name__ == '__main__':
#     workbook = xlsxwriter.Workbook("testcase.xlsx")
#     writeTestcase().create_worksheet2(workbook)
#     yamlFile = "F:\\PythonWorkSpace\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\settings\\01_wifi.yaml"
#     result_tuple = 1, 2, 3
#     writeTestcase().worksheet2_write_data(workbook, yamlFile)
#     workbook.close()

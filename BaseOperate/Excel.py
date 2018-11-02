# coding: utf-8
import time
import xlsxwriter
import os
import datetime
from BaseOperate.get_testcaseyaml_info import getyamlInfo
from BaseOperate.MachineInfo import machine
from BaseOperate.run import run_testcaseYaml


class Report:
    initRow = 2
    workbook = xlsxwriter.Workbook('')
    startTime = datetime.datetime.now()
    init_caseNum = 0

    # def __init__(self):
    #     self.keyValue = {}
    #     self.position = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    #     self.key = ['caseTitle', 'caseCondition', 'caseSteps', 'caseCheck', 'caseResult', 'remarks', 'screenshot']

    def create_workbook(self):
        now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        Report.excelName = "Report-" + now + ".xlsx"
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p))
        excelPath = PATH('../results/report/')
        excelFile = os.path.join(excelPath, Report.excelName)
        print(excelFile)
        Report.workbook = xlsxwriter.Workbook(excelFile)  # 创建excel对象
        return Report.workbook

    def set_Workbookformat_subject(self):
        # 设置单元格格式: 表格中主题格式
        workbook_subject_format = Report.workbook.add_format(
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

    def set_Workbookformat_content(self):
        # 设置单元格格式: 表格中其它内容格式
        workbook_content_format = Report.workbook.add_format(
            {
                'align': 'center',  # 水平居中
                'font_size': 10,
                'border': 1,
                'valign': 'vcenter',  # 垂直居中
                'text_wrap': 1  # 自动换行
            })
        return workbook_content_format

    def create_worksheet1(self):
        subject_formate = self.set_Workbookformat_subject()
        content_formate = self.set_Workbookformat_content()
        worksheet1 = Report.workbook.add_worksheet("测试总结")  # 创建sheet表单对象
        # 设置列和行的宽度高度
        worksheet1.set_column('A:D', 20)
        for i in range(10):
            worksheet1.set_row(i, 30)
        # 设置第一行总标题
        worksheet1.merge_range('A1:D1', u'测试结果概况', subject_formate)
        # 所需显示的内容标题
        title = ['机器型号', '产品名称', '软件版本', '测试日期', '用例总数', '通过总数', '失败总数', '通过率']
        worksheet1.write('A2', title[0], content_formate)
        worksheet1.write('A3', title[1], content_formate)
        worksheet1.write('A4', title[2], content_formate)
        worksheet1.write('A5', title[3], content_formate)
        worksheet1.write('C2', title[4], content_formate)
        worksheet1.write('C3', title[5], content_formate)
        worksheet1.write('C4', title[6], content_formate)
        worksheet1.write('C5', title[7], content_formate)

    def worksheet1_write_data(self):
        content_formate = self.set_Workbookformat_content()
        worksheet1 = Report.workbook.get_worksheet_by_name("测试总结")
        data = {'deviceModel': '', 'productName': '', 'softwareVersion': '', 'testDate': '',
                'sum': '', 'pass': '', 'fail': '', 'passPercent': ''}
        # 所需填写的结果
        data['deviceModel'] = machine().get_productModel()
        data['productName'] = machine().get_productName()
        data['softwareVersion'] = machine().get_softwareVersion()
        data['testDate'] = str(Report.startTime)
        data['sum'] = Report.init_caseNum
        data['pass'] = run_testcaseYaml.passNum
        data['fail'] = run_testcaseYaml.failNum
        passPercent = '%.2f' % (int(data['pass']) / int(data['sum']) * 100)
        data['passPercent'] = str(passPercent) + "%"
        print(data)
        worksheet1.write('B2', data['deviceModel'], content_formate)
        worksheet1.write('B3', data['productName'], content_formate)
        worksheet1.write('B4', data['softwareVersion'], content_formate)
        worksheet1.write('B5', data['testDate'], content_formate)
        worksheet1.write('D2', data['sum'], content_formate)
        worksheet1.write('D3', data['pass'], content_formate)
        worksheet1.write('D4', data['fail'], content_formate)
        worksheet1.write('D5', data['passPercent'], content_formate)

    def create_worksheet2(self):
        subject_formate = self.set_Workbookformat_subject()
        content_formate = self.set_Workbookformat_content()
        worksheet2 = Report.workbook.add_worksheet("测试详情")  # 创建sheet表单对象
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

    def worksheet2_write_data(self, yamlFile, actualResult_List, resultOutput, testConclusion):
        Report.initRow += 1
        Report.init_caseNum += 1
        row = Report().initRow
        content_formate = self.set_Workbookformat_content()
        worksheet2 = Report.workbook.get_worksheet_by_name("测试详情")
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
        # 传入case标题和条件
        data['caseTitle']['value'] = getyamlInfo(yamlFile).get_title()
        data['caseCondition']['value'] = getyamlInfo(yamlFile).get_condition()
        # 传入测试步骤
        step = ""
        i = 1
        caseLength = len(getyamlInfo(yamlFile).get_testcaseData())
        if i <= caseLength:
            for key in getyamlInfo(yamlFile).get_testcaseData().keys():
                step += str(i) + '.' + getyamlInfo(yamlFile).get_operate_details(key) + '\n'
                i += 1
        data['caseSteps']['value'] = step
        # 传入测试检查点
        check = ""
        i = 1
        caseLength = len(getyamlInfo(yamlFile).get_checkDate())
        if i <= caseLength:
            for key in getyamlInfo(yamlFile).get_checkDate().keys():
                check += str(i) + '.' + getyamlInfo(yamlFile).get_check_content(key) + '\n'
                i += 1
        data['caseCheck']['value'] = check
        # 传入期待结果
        expectResult = ""
        i = 1
        caseLength = len(getyamlInfo(yamlFile).get_checkDate())
        if i <= caseLength:
            for key in getyamlInfo(yamlFile).get_checkDate().keys():
                expectResult += str(i) + '.' + getyamlInfo(yamlFile).get_expect_value(key) + '\n'
                i += 1
        elif caseLength == 0:
            expectResult = "空"
        data['expectResult']['value'] = expectResult

        # 传入实际结果
        actualResult = ""
        actualResult_length = len(actualResult_List)
        if actualResult_length == 0:
            actualResult = "空"
        else:
            for i in range(actualResult_length):
                actualResult += str(i + 1) + '.' + actualResult_List[i] + '\n'
        data['actualResult']['value'] = actualResult

        # 传入运行结果
        data['resultOutput']['value'] = resultOutput
        # 传入测试结论
        data['testConclusion']['value'] = testConclusion

        for key in data.keys():
            location = data[key]['position']
            value = data[key]['value']
            worksheet2.write(location, value, content_formate)

    def closeWorkbook(self):
        Report.workbook.close()

# if __name__ == "__main__":
#     # data1 = {'testDevice': '', 'testMode': '', 'software': '', 'testDate': '',
#     #          'sum': '', 'pass': '', 'fail': '', 'testSumTime': ''}
#     # data2 = {'caseTitle': '', 'caseCondition': '', 'caseSteps': '',
#     #          'caseCheck': '', 'runResult', 'caseResult': '', 'remarks': '', 'screenshot': ''}
#     yamlFile = "E:\\PycharmProjects\\appium_yaml_autoTest_addCheck\\common\\testcaseyaml\\xiSettings\\01_wifi.yaml"
#     result = "True"
#     workbook = Report().create_workbook()
#     Report().create_worksheet1(workbook)
#     Report().worksheet1_write_data(workbook)
#
#     Report().create_worksheet2(workbook)
#     Report().worksheet2_write_data(3, yamlFile, '1', '2', 'PASS', workbook)
#     Report().worksheet2_write_data(4, yamlFile, '1', '2', 'PASS', workbook)
#     Report().closeWorkbook(workbook)

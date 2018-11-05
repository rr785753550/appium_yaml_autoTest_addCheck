import xlsxwriter


class AddChartInExcel:
    startPoint = 'A'

    def addChart(self, workbook, charTitle, yData, xName, yName):
        worksheet = workbook.add_worksheet("top")
        bold = workbook.add_format({'bold': 1})     # 自定义格式，加粗
        # Add the worksheet data that the charts will refer to.
        headings = [charTitle]
        dataLength = len(yData)
        worksheet.write_row('A1', headings, bold)   # 从A1位置开始横向把内容标题写入
        worksheet.write_column('A2', yData)         # 从A2纵向把内容写入
        # startPoint = AddChartInExcel.startPoint
        # worksheet.write_row(startPoint + str(1), headings, bold)
        # worksheet.write_column(startPoint + str(2), yData)

        # Create a new chart object. In this case an embedded chart.创建一个线性图
        chart1 = workbook.add_chart({'type': 'line'})

        # Configure the first series.
        # chart1.add_series({
        #     'name': '=Sheet1!$B$1',
        #     'categories': '=Sheet1!$A$1:$A$' + str(xDataLength),
        #     'values': '=Sheet1!$B$1:$B$' + str(xDataLength),
        # })

        # Configure second series. Note use of alternative syntax to define ranges.
        chart1.add_series({
            'name': [charTitle, 0, 1],
            # 'categories': [charTitle, 1, 0, dataLength, 0],
            'values': [charTitle, 1, 0, dataLength, 0],
        })

        # Add a chart title and some axis labels.设置图表的title、x和y轴信息
        chart1.set_title({'name': charTitle})
        chart1.set_x_axis({'name': xName})
        chart1.set_y_axis({'name': yName})

        # Set an Excel chart style. Colors with white outline and shadow.设置图表风格
        chart1.set_style(10)

        # Insert the chart into the worksheet (with an offset).将图表插入到worksheet中并设置偏移
        worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

        # startPoint = chr(ord(startPoint) + 1)   # ASCII值和字符值转换
        # print(startPoint)
        # return workbook
        workbook.close()

if __name__ =="__main__":
    workbook = xlsxwriter.Workbook('testAddExcel.xlsx')

    # xData = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    yData = [17, 13, 0, 0, 11, 11, 0, 0, 22, 12, 22, 16, 16, 17, 12, 14, 18, 31, 27, 27, 13, 19, 15, 17, 17, 16, 0, 0, 0, 13, 14, 0, 18, 14, 12, 12]
    # workbook对象，sheet名字，x轴数据数组，y轴数据数组，x轴title，y轴title,
    # AddChartInExcel().addChart(workbook, 'app.cpu.info', yData, 'number', 'CPU%')
    # AddChartInExcel().addChart(workbook, 'app.cpu.info', yData, 'number', 'CPU%')
    # workbook.close()

    AddChartInExcel().addChart(workbook, 'app.cpu.info', yData, 'number', 'CPU%')

    # ？？？表格名称不可以含 /还需更改

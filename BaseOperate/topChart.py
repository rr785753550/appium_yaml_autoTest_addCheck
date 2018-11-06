import xlsxwriter


class Add_topChart:
    writePoint = 'A'
    writePoint1 = 'AA'
    writePoint2 = 'BA'
    writePoint3 = 'CA'
    writeTimes = 0

    def get_writePoint(self):
        Add_topChart.writeTimes += 1
        i = Add_topChart.writeTimes
        # print(i)
        if i == 1:
            # print(AddChartInExcel.writePoint)
            return Add_topChart.writePoint
        elif 1 < i < 27:
            p = Add_topChart.writePoint
            position = chr(ord(p[0]) + 1)  # ASCII值与字符串的转换
            # print(position)
            Add_topChart.writePoint = position
            return Add_topChart.writePoint
        elif i == 27:
            # print(AddChartInExcel.writePoint1)
            return Add_topChart.writePoint1
        elif 27 < i < 53:
            p = Add_topChart.writePoint1
            position = p[0] + chr(ord(p[1]) + 1)
            # print(position)
            Add_topChart.writePoint1 = position
            return Add_topChart.writePoint1
        elif i == 53:
            # print(AddChartInExcel.writePoint2)
            return Add_topChart.writePoint2
        elif 53 < i < 79:
            p = Add_topChart.writePoint2
            position = p[0] + chr(ord(p[1]) + 1)
            # print(position)
            Add_topChart.writePoint2 = position
            return Add_topChart.writePoint2
        elif i == 79:
            # print(AddChartInExcel.writePoint3)
            return Add_topChart.writePoint3
        elif 79 < i < 105:
            p = Add_topChart.writePoint3
            position = p[0] + chr(ord(p[1]) + 1)
            # print(position)
            Add_topChart.writePoint2 = position
            return Add_topChart.writePoint3

    def addChart(self, workbook, charTitle, yData, index):
        sheetName = "topChart"
        writePoint = self.get_writePoint()
        # print(writePoint)
        worksheet = workbook.get_worksheet_by_name(sheetName)
        bold = workbook.add_format({'bold': 1})  # 自定义格式，加粗
        # 向excel表格中添加数据
        headings = [charTitle]
        dataLength = len(yData)
        worksheet.write_row(writePoint + str(1), headings, bold)  # 从A1位置开始横向把内容标题写入
        worksheet.write_column(writePoint + str(2), yData)  # 从A2纵向把内容写入
        chart1 = workbook.add_chart({'type': 'line'})   # 创建一个线性图
        chart1.add_series({
            # 'name': [sheetName, 0, 1],
            'values': [sheetName, 1, index, dataLength, index],
        })
        # 设置图表的title、x和y轴信息
        chart1.set_title({'name': charTitle})
        chart1.set_x_axis({'name': "number"})
        chart1.set_y_axis({'name': 'CPU%'})
        # 将图表插入到worksheet中并设置偏移
        xOffset = 25
        yOffset = 10
        if index % 2 == 0:
            yOffset += index * (yOffset + chart1.height)
        else:
            yOffset += (index - 1) * (yOffset + chart1.height)
            xOffset += chart1.width
        worksheet.insert_chart('D2', chart1, {'x_offset': xOffset, 'y_offset': yOffset})
        # print(xOffset, yOffset)

    def readTop_byName(self):
        from BaseOperate.grabTop import top
        data = top().read_topText()[1:]
        print(data)
        name_list = []
        for i in range(len(data)):
            name_list.append(data[i][9])
        # print(name_list)
        name_only_list = list(set(name_list))  # 筛选列表中内容不重复的为新列表
        name_only_list.sort(key=name_list.index)
        # print(name_only_list)
        cpuDict = {}
        for i in range(len(name_only_list)):
            temp = []
            for j in range(len(data)):
                if name_only_list[i] == data[j][9]:
                    temp.append(data[j][2])
            # print(temp)
            cpuDict[name_only_list[i]] = temp
        print(cpuDict)  # 分隔以name分隔出所抓取的cpu数据
        return cpuDict

    def excel_insert_topChart(self, workbook):
        cpuDict = self.readTop_byName()
        index = 0
        for key in cpuDict.keys():
            key_values = cpuDict.get(key)
            # print(key_values)
            y_values = []
            for i in range(len(key_values)):
                tmp = int(key_values[i].split("%")[0])
                y_values.append(tmp)
            # print(key)
            # print(y_values)
            if len(y_values) > 5:   # 仅统计cpu信息超过5个的app
                self.addChart(workbook, key, y_values, index)
                index = index + 1


# if __name__ == "__main__":
#     workbook = xlsxwriter.Workbook('testAddExcel.xlsx')
#     worksheet = workbook.add_worksheet("topChart")
#     # xData = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#     # workbook对象，sheet名字，x轴数据数组，y轴数据数组，x轴title，y轴title,
#     # yData = [13, 1, 0, 0, 11, 11, 0, 0, 1, 12, 22, 16, 16, 2, 12, 14, 18, 31, 27, 27, 13, 19, 15, 17, 17, 3, 0, 0]
#     # AddChartInExcel().addChart('app.cpu.info', yData)
#     Add_topChart().excel_insert_topChart(workbook)
#     workbook.close()

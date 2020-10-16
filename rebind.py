from os import walk
import xlrd
import xlsxwriter

def rebinds(dir):
    global files
    for root, dirs, files, in walk(dir, topdown=False):
        print(files)
    num = len(files)
    # 读取数据
    data = []
    for i in range(num):
        wb = xlrd.open_workbook(dir + r'/%s' %files[i])
        for sheet in wb.sheets():
            for rownum in range(sheet.nrows):
                data.append(sheet.row_values(rownum))
    # 写入数据
    workbook = xlsxwriter.Workbook(dir + r'/output.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(len(data)):
        for j in range(len(data[i])):
            worksheet.write(i, j, data[i][j])
    # 关闭文件流
    workbook.close()

def helloWorld(flag):
    if flag == 1:
        print("Hello")
    elif flag == 0:
        print("World")
    else:
        print("Wrong")
# -*- coding: utf-8 -*-
# @Time : 2020/3/12 11:02
# @Author : 52595
# @File : 20200310_4.py
# @Python Version : 3.7.4
# @Software: PyCharm
import datetime

import requests
import json
import urllib3
import openpyxl
import prettytable
from pip._vendor.distlib.compat import raw_input

'''
--功能描述：
            提取12036查询页面中的车次信息，不用人为的录入数据。
--注意事项：
            1、需要获取页面的查询路径，即url_query字段的值。
            2、浏览器的cookies的值。
            3、使用狐火浏览器方便查看json格式中的内容。

--学习内容：
            1、根据url请求，获取页面中信息。
            2、json格式的转换以及json内容的读取
            备注：关键看怎么读取内容，因为如果换一个静态页面，自己是否也能进行爬取
            3、excel文件内容的读写操作

update history:
    20191225,打开excel文件后，执行程序包，由于软件已打开，导致程序出错。改为文件名自动生成
                知识点：（1）解析url,获取传入的参数值
                        （2）日期类使用，获取当前时间
                        （3）数据结构：列表、字典的使用
'''


# 往Excel中写内容，参数1：excel写入的路径；参数2：excel工作表名称；参数3：需要写入的具体值
# 注意事项：如果执行代码前打开该Excel，则执行代码会报错
def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    workbook.save(path)
    print("xlsx格式表格写入数据成功！")


# 根据页面中信息，解析成json格式，然后返回车次信息
def show_ticket():
    # 获取完成，存放在字典中
    # 本地读取内容
    # 注意更换此处内容
    cookies = 'JSESSIONID=6E3CEBE74D8037D5AD40A87AED10575C; RAIL_EXPIRATION=1577248851714; RAIL_DEVICEID=XOLNCis8hBr_3hvhlCqUagaLiAekZrudBOROBm9OthStqgetYm9SArlaelgL43DtRpJxrEzxQhvQEdXoavu-bCe11MUQuWQe8HQhta2F_Ro_WYg1MKhpFYjRqCU44KqZBI0SG5Lr5mDTbSXLl6cNb5cxjyTaGxAr; _jc_save_fromStation=%u6B66%u6C49%2CWHN; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2020-01-23; _jc_save_toDate=2019-12-25; _jc_save_wfdc_flag=dc; BIGipServerotn=1022362122.64545.0000; BIGipServerpool_passport=267190794.50215.0000; route=6f50b51faa11b987e576cdb301e545c4'

    # 获取当前站点代码对应的站点中文名  begin
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9130'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url_tmp = str(requests.get(url, verify=False).content, encoding='utf-8').replace("var station_names ='@",
                                                                                     '').replace(
        "';", '')
    url_tmp = list(url_tmp.split('@'))
    # 返回字典类型的本地变量
    # 比如i =5 str ='2'
    # 使用local()返回，{'i':5 , 'str':'2'}
    # dict_station = locals()
    # ---------------------------
    dict_station = dict()
    # 手动输入站点，获取对应站点代码
    dict_station_to_code = dict()
    for i in url_tmp:
        dict_station[i.split('|')[2]] = i.split('|')[1]
        dict_station_to_code[i.split('|')[1]] = i.split('|')[2]
    # 手动收入起始站，终点站
    strInput = raw_input("请输入起始站，终点站（空格分隔）：")
    strInputList = list()
    # 空格没有全角和半角之分
    # print(strInput.find(' '))
    if strInput.find(' ') > 0:
        strInputList = strInput.split(' ')
    else:
        print('输入格式有误')
        exit(1)
    from_station_code = ''
    to_station_code = ''
    # 为何定义dict才能使用has_key
    # dict = dict_station_to_code
    # 获取当前站点代码对应的站点中文名  end
    # if dict.has_key(strInputList[0]) & dict.has_key(strInputList[1]):
    from_station_code = dict_station_to_code.get(strInputList[0])
    to_station_code = dict_station_to_code.get(strInputList[1])
    if from_station_code is None or to_station_code is None :
        print('输入站点信息有误，请检查')
        # 0正常退出，1异常退出
        exit(1)
    header = {
        'Cookie': cookies,
        'Host': 'kyfw.12306.cn',
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
        'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        # Firefox表示火狐
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
        # Chrome表示谷歌
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    # 后去当前时间的后一天，防止查询车次信息不完整
    str_now_time = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")
    url_query = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(str_now_time, from_station_code, to_station_code)
    # print(url_query)
    response = requests.get(url_query, headers=header)
    # html，返回一个Json格式
    html = json.loads(response.content)
    # print(html)
    table_top = [" 车次 ", "出发车站", "到达车站", "出发时间", "到达时间", " 历时 "]
    tickets_excel = list()
    # list中可以嵌套list
    tickets_excel.append(table_top)
    name = [
        "station_train_code",
        "from_station_name",
        "to_station_name",
        "start_time",
        "arrive_time",
        "lishi"
    ]
    data = {
        "station_train_code": '',
        "from_station_name": '',
        "to_station_name": '',
        "start_time": '',
        "arrive_time": '',
        "lishi": ''
    }

    table = prettytable.PrettyTable([" 车次 ", "出发车站", "到达车站", "出发时间", "到达时间", " 历时 "])
    for i in html['data']['result']:
        # 将各项信息提取并赋值
        item = i.split('|')  # 使用“|”进行分割
        # split函数能将字符串根据某字符进行分割，然后返回一个数组
        data["station_train_code"] = item[3]  # 获取车次信息，在3号位置
        data["from_station_name"] = item[6]  # 始发站信息在6号位置
        data["to_station_name"] = item[7]  # 终点站信息在7号位置
        data["start_time"] = item[8]  # 出发时间在8号位置
        data["arrive_time"] = item[9]  # 抵达时间在9号位置
        data["lishi"] = item[10]  # 经历时间在10号位置
        # color = Colored()
        # data["note_num"] = color.white(item[1])
        # 如果没有信息，那么就用“-”代替
        for pos in name:
            if data[pos] == "":
                data[pos] = "-"
        tickets = []
        # tickets.append(tableTop)
        cont = list()
        cont.append(data)
        # 循环的目的，数据处理，对于车次信息，换算成具体的车站名称  lwc,20191223
        for x in cont:
            tmp = []
            for y in name:
                # 起点站
                if y == "from_station_name":
                    # s = color.green(chezhan_names[data["from_station_name"]])
                    s1 = dict_station[data["from_station_name"]]
                    tmp.append(s1)
                # 终点站
                elif y == "to_station_name":
                    # s = color.red(chezhan_names[data["to_station_name"]])
                    s1 = dict_station[data["to_station_name"]]
                    tmp.append(s1)
                # 起始时间
                elif y == "start_time":
                    # s = color.green(data["start_time"])
                    s1 = data["start_time"]
                    tmp.append(s1)
                # 到达时间
                elif y == "arrive_time":
                    # s = color.red(data["arrive_time"])
                    s1 = data["arrive_time"]
                    tmp.append(s1)
                # 车次信息
                elif y == "station_train_code":
                    # s = color.yellow(data["station_train_code"])
                    s1 = data["station_train_code"]
                    tmp.append(s1)
                elif y == "lishi":
                    s1 = data["lishi"]
                    tmp.append(s1)
            # print(tmp)
        tickets_excel.append(tmp)
    return tickets_excel


# -------------------------具体的传参以及代码执行过程-------------------------------------------
# 车次信息输出Excel的路径
# 每次由于指定输出文件，由于打开，导致执行程序报错
# 拼接后的Excle路径以及名称
train_name_xlsx = 'D:\\developmentSoft\\pythonWorkspace\\trainInfo\\123456_trainInfo.xlsx'

# 工作表的名称
sheet_name_xlsx = "车次信息"

# 开始调用函数
# 1、获取页面中的数据，并提取车次信息并返回
value3 = show_ticket()

# 2、将获取到的数据写入Excel中，若需要读取Excel中的内容，则放开第3步的代码
# 注意事项，打开excel后，允许此程序则会报错 ，写入 20191224
# 文件名称自动生成   20191225
write_excel_xlsx(train_name_xlsx, sheet_name_xlsx, value3)
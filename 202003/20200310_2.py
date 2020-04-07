# -*- coding: utf-8 -*-
# @Time : 2020/3/11 17:32
# @Author : 52595
# @File : 20200310_2.py
# @Python Version : 3.7.4
# @Software: PyCharm
import json
import math
import re

import pandas as pd
import requests

fundCode = '000001'
pageIndex = 1
url = 'http://api.fund.eastmoney.com/f10/lsjz'

# 参数化访问链接，以dict方式存储
params = {
    'callback': 'jQuery18307633215694564663_1548321266367',
    'fundCode': fundCode,
    'pageIndex': pageIndex,
    # 每页的数量
    'pageSize': 1,
}
# 存储cookie内容
cookie = 'EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null; EMFUND0=null; EMFUND9=01-24 17:11:50@#$%u957F%u4FE1%u5229%u5E7F%u6DF7%u5408A@%23%24519961; st_pvi=27838598767214; st_si=11887649835514'
# 装饰头文件
headers = {
    'Cookie': cookie,
    'Host': 'api.fund.eastmoney.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % fundCode,
}
r = requests.get(url=url, headers=headers, params=params)  # 发送请求
# print(r.text)
text = re.findall('\((.*?)\)', r.text)[0]  # 提取dict
LSJZList = json.loads(text)['Data']['LSJZList']  # 获取历史净值数据
print(LSJZList[0])
print(LSJZList[0]['FSRQ'])
print(LSJZList[0]['JZZZL'])

# TotalCount = json.loads(text)['TotalCount']  # 转化为dict
# LSJZ = pd.DataFrame(LSJZList)  # 转化为DataFrame格式
# print(LSJZ)
# LSJZ['fundCode'] = fundCode  # 新增一列fundCode
# total_page = math.ceil(total_count / 20)
# list中嵌套list
table_top = [" 日期 ", "基金代码", "基金名称", "涨幅"] #对应 FSRQ  传入参数  传入参数转换  JZZZL
tickets_excel = list()
# list中可以嵌套list
tickets_excel.append(table_top)
foundation = list()
foundation.append(LSJZList[0]['FSRQ'])
foundation.append('00001')
foundation.append('测试')
foundation.append(LSJZList[0]['JZZZL'])
tickets_excel.append(foundation)
print(tickets_excel)



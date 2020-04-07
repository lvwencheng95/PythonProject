# -*- coding: utf-8 -*-
# @Time : 2020/3/11 22:18
# @Author : 52595
# @File : 20200310_3.py
# @Python Version : 3.7.4
# @Software: PyCharm
'''
优化：（1）变量名更改
    （2）此处cookies为何可以直接使用，而不用copy浏览器中内容，联想到12306中还需要拷贝，可互相联系

    类型转换;[fd] = ls[int(fd) - 1][2]
参考资料：https://www.cnblogs.com/xmyzero/p/10319962.html
'''
import re
import json
from prettytable import PrettyTable
import pandas as pd
import requests

# 获取当前基金代码对应的基金中文名称
r = requests.get('http://fund.eastmoney.com/js/fundcode_search.js')
# print(r.text)
# 提取list
cont = re.findall('var r = (.*])', r.text)[0]
ls = json.loads(cont)  # 将字符串个事的list转化为list格式
# print(ls)

myFoundationCode = ['160222', '502010', '110003', '006748', '001594']
# myFoundationCode = ['006748', '001594']
dic = dict()
count_i = 0
# 需要查询的基金代码
myFoundationCodeCopy = myFoundationCode.copy()
# 基金不是按照1到后面顺序排列（1，2，3，4，5，6...）
# 循环基金代码表，并有当前需要查询的基金代码进行比对
for ls_fd in ls:
    # 若找到所需查询的基金代码对应描述，则停止循环
    if count_i == len(myFoundationCode):
        break
    else:
        for fd in myFoundationCodeCopy:
            if ls_fd[0] == fd:
                dic[fd] = ls_fd[2]
                # 减少循环次数，找到后，移除，减少下次比较次数
                myFoundationCodeCopy.remove(fd)
                # 判断需要查找的基金数
                count_i = count_i + 1
                break
# 内容输出
'''
for fd in myFoundationCode:
    print(fd)
    print(dic[fd])
'''
url = 'http://api.fund.eastmoney.com/f10/lsjz'

# 存储cookie内容
cookie = 'EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null; EMFUND0=null; EMFUND9=01-24 17:11:50@#$%u957F%u4FE1%u5229%u5E7F%u6DF7%u5408A@%23%24519961; st_pvi=27838598767214; st_si=11887649835514'

# list中嵌套list
table_top = [" 日期 ", "基金代码", "基金名称", "涨幅"]  # 对应 FSRQ  传入参数  传入参数转换  JZZZL
# 保存查询记录了信息，包括列头，该list中包含list
fdListShow = list()
# list中可以嵌套list
fdListShow.append(table_top)
for fd in myFoundationCode:
    fundCode = fd
    pageIndex = 1
    # 参数化访问链接，以dict方式存储
    params = {
        'callback': 'jQuery18307633215694564663_1548321266367',
        'fundCode': fundCode,
        'pageIndex': pageIndex,
        # 每页的数量
        'pageSize': 1,
    }
    # 装饰头文件
    headers = {
        'Cookie': cookie,
        'Host': 'api.fund.eastmoney.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % fundCode,
    }
    r = requests.get(url=url, headers=headers, params=params)  # 发送请求
    text = re.findall('\((.*?)\)', r.text)[0]  # 提取dict
    LSJZList = json.loads(text)['Data']['LSJZList']  # 获取历史净值数据
    foundation = list()
    foundation.append(LSJZList[0]['FSRQ'])
    foundation.append(fundCode)
    foundation.append(dic[fundCode])
    foundation.append(LSJZList[0]['JZZZL'])
    fdListShow.append(foundation)
# print(tickets_excel)
table = PrettyTable(fdListShow[0])
for i in range(1, len(fdListShow)):
    table.add_row(fdListShow[i])
print(table)

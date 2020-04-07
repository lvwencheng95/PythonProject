# -*- coding: utf-8 -*-
# @Time : 2020/3/11 17:11
# @Author : 52595
# @File : 20200310_1.py
# @Python Version : 3.7.4
# @Software: PyCharm
import json
import re

import pandas as pd
import requests
r = requests.get('http://fund.eastmoney.com/js/fundcode_search.js')
# print(r.text)
# 提取list
cont = re.findall('var r = (.*])', r.text)[0]
ls = json.loads(cont)  # 将字符串个事的list转化为list格式
# all_fundCode = pd.DataFrame(ls, columns=['基金代码', '基金名称缩写', '基金名称', '基金类型', '基金名称拼音'])  # list转为DataFrame
# 有规律，排序的，比如000001可看成1，则在序号为0（1-1）中进行查找
print(ls[0][0])
print(ls[0][2])
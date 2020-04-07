# -*- coding: utf-8 -*-
# @Time : 2020/3/12 22:28
# @Author : 52595
# @File : 20200310_5.py
# @Python Version : 3.7.4
# @Software: PyCharm
import datetime

# 时间类datetime的使用
str_now_time = datetime.datetime.now().__format__('%Y%m%d_%H%M_%S')
print(str_now_time)
str_now_time = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M:%S")
print(str_now_time)
dict = {'1': 1, 'b': 2}
# python2中使用has_key()
# print(dict.has_key('1')) # 在python3中提示语法错误
# python3中使用以下方式
if '1' in dict:
    print('key为1存在')
age = 10
year = '2020'
print('%s年,我%d岁' % (year, age))
str1 = '1'
print(int(str1)+1)
print(type(str(int(str1)+1)))


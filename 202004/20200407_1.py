# -*- coding: utf-8 -*-
# @Time : 2020/4/7 14:42
# @Author : 52595
# @File : 20200407_1.py
# @Python Version : 3.7.4
# @Software: PyCharm

import matplotlib.pyplot as plt

names = ['201907', '201908', '201909', '201910', '201911', '201912', '202001', '202002', '202003']
x = range(len(names))
y = [350.68, 1124.1, 560.24, 355.8, 1011.14, 886.57, 611.39, 1000, 192.3]
y1 = [100, 1300, 400, 300, 1000, 900, 600, 900, 200]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
# 设置折现表的标题，并给定字号,设置颜色
plt.title("支出情况一览表", fontsize=24, color='black')
# 为折线图色的纵坐标设置标题
plt.ylabel("金额", fontsize=14, color='black')
plt.plot(x, y, 'ro-')
plt.plot(x, y1, 'blue')
plt.xticks(x, names, rotation=45)
plt.margins(0.08)
plt.subplots_adjust(bottom=0.15)
plt.show()

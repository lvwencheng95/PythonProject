# -*- coding: utf-8 -*-
# @Time : 2020/4/7 16:16
# @Author : 52595
# @File : ZheXianTu.py
# @Python Version : 3.7.4
# @Software: PyCharm
"""
    功能描述：根据每月消费情况，绘制折线图，方面查看
"""
import matplotlib.pyplot as plt

# names = range(8, 21)
# names = [str(x) for x in list(names)]
names = ['201907', '201908', '201909', '201910', '201911', '201912', '202001', '202002', '202003']
x = range(len(names))
# 残影美食
y_food_drink = [350.68, 1124.1, 560.24, 355.8, 1011.14, 886.57, 611.39, 1000, 192.3]
# 日常消费
y_daily_consumption = [772.38, 738.4, 215.53, 1199.85, 509.67, 1185.64, 50.5, 72.52, 221.89]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x, y_food_drink, marker='o', mec='r', mfc='w', label='餐饮美食')
plt.plot(x, y_daily_consumption, marker='*', ms=10, label='日常消费')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=1)

plt.margins(0)
plt.subplots_adjust(bottom=0.10)
plt.title("支出情况一览表", fontsize=24, color='black')  # 折线图绘制描述描述信息
plt.xlabel('年月')  # X轴标签
plt.ylabel("金额")  # Y轴标签
plt.show()

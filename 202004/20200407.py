# -*- coding: utf-8 -*-
# @Time : 2020/4/7 14:19
# @Author : 52595
# @File : 20200407.py
# @Python Version : 3.7.4
# @Software: PyCharm
import matplotlib.pyplot as plt

# 创建一个数组列表
values = [1, 2, 3, 4, 5]  # 纵坐标
square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 横坐标
# 将列表传递给plot,并设置线宽，设置颜色，默认为蓝色
plt.plot(values, square, linewidth=5, color='b')
# 给折线表设置标题，并给定字号,设置颜色
plt.title("Squares Number", fontsize=24, color='r')
plt.title("Squares Number", fontsize=24, color='r')
plt.xlabel("Value", fontsize=14, color='g')
# 设置轴标题，并给定字号,设置颜色
plt.ylabel("Squares Of Value", fontsize=14, color='g')
plt.tick_params(axis='both', labelsize=14)
# 设置刻度标记的大小
plt.show()
# 显示

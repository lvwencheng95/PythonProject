# -*- coding: utf-8 -*-
# @Time : 2019/12/24 15:41
# @Author : 52595
# @File : 20191224_2.py
# @Software: PyCharm
"""
    函数的定义，对于形参能给定默认值，若不修改默认值，则不用传入该字段值
"""


# 参数1：提示信息。参数2：允许尝试的错误。 参数3：提示输入内容。
# 参数2、参数3，存在默认值
def ask_ok(prompt, retries=4, complaint='Yes or no,please!'):
    while True:
        # 控制台中输入内容
        ok = input(prompt)
        # 如果满足则退出，并返回True
        if ok in ('y', 'ye', 'yes'):
            return True
        # 如果满足则退出，并返回False
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        # 设置输入次数，次数到达，则提示报错
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


# 一个参数，提示信息
# ask_ok('Do you really want to quit?')
# 两个参数，提示信息，尝试错误的次数.传入值为1，则只允许输入一次
# ask_ok('Do you really want to quit?', 1)
# 三个参数
ask_ok('Do you really want to quit?', 2, '输入yes或no')

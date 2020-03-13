# -*- coding: utf-8 -*-
# @Time : 2020/3/12 22:28
# @Author : 52595
# @File : 20200310_5.py
# @Python Version : 3.7.4
# @Software: PyCharm


# str_now_time = datetime.now().__format__('_%Y%m%d_%H%M_%S')
import datetime

import datetime as datetime

str_now_time = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d %H:%M:%S")
print(str_now_time)
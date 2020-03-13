# -*- coding: utf-8 -*-
# @Time : 2020/2/24 10:30
# @Author : 52595
# @File : 20200224_1.py
# @Python Version : 3.7.4
# @Software: PyCharm

import requests
url = 'https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=2020-03-11&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=SZQ&purpose_codes=ADULT'
res = requests.get(url)
print(res.cookies)
print(type(res.cookies))
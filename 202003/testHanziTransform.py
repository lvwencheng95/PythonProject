# -*- coding: utf-8 -*-
# @Time : 2020/3/18 17:18
# @Author : 52595
# @File : testHanziTransform.py
# @Python Version : 3.7.4
# @Software: PyCharm
import binascii
import json
"""
学习内容;   1、编码格式的转换
           2、字符串的截取  a[x:y]
           3、字符串、列表、字典间的转换
           参考资料：https://www.cnblogs.com/who-care/p/9306800.html
"""
import requests

url_query = 'https://bihua.51240.com/web_system/51240_com_www/system/file/bihua/get_0/?font=e6b189&shi_fou_zi_dong=1&cache_sjs1=20031901'
# cooky11 = 'Hm_lvt_fbe0e02a7ffde424814bef2f6c9d36eb=1584433904,1584520595; __gads=ID=a14a729f79924a24:T=1584520596:S=ALNI_MZGE-F7i75SaXjljA_Kzenbzmxn-w; c_y_g_j=bihua%2Czhongwenzhuanpinyin'
cooky11 = 'Hm_lvt_fbe0e02a7ffde424814bef2f6c9d36eb=1584433904,1584520595,1584541953,1584799808; __gads=ID=a14a729f79924a24:T=1584520596:S=ALNI_MZGE-F7i75SaXjljA_Kzenbzmxn-w; Hm_lpvt_fbe0e02a7ffde424814bef2f6c9d36eb=1584800309; c_y_g_j=bihua%2Czhongwenzhuanpinyin'
header = {
    'Cookie': cooky11,
    'Host': 'bihua.51240.com',
    'Referer': 'https://bihua.51240.com/e5bca0__bihuachaxun/',
    # Firefox表示火狐
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    # Chrome表示谷歌
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
response = requests.get(url_query, headers=header)
response_content = response.content.decode("utf-8")
# 由于返回不是json格式内容，因此无法进行转换
# html = json.loads(response.content)
# hzbh.main('张',{张:[7,'cjzsjhl','0:(36,96) (240,96) (276,72) (240,96) (240,300)#1:(90,270) (240,270)#2:(72,678) (150,744) (198,696) (222,432) (252,408) (222,432) (72,432) (54,450) (72,432) (90,270) (90,228)#3:(618,78) (660,102) (588,180) (504,258) (402,336)#4:(264,372) (708,372) (660,354) (612,372)#5:(366,30) (402,54) (402,738) (390,756) (402,738) (534,630)#6:(468,372) (492,438) (522,498) (570,570) (636,642) (714,702)','zhàng、zhāng']});document.getElementById("tianzi_jie_guo_dixiabeizhu").innerHTML = "一共<b>1</b>个汉字，共计笔画：<b>7</b>画";
# print(response_content.index('[', 0, len(response_content)))
# print(response_content.index('}', 0, len(response_content)))
l_index = response_content.index('[', 0, len(response_content))
r_index = response_content.index('}', 0, len(response_content))
# print(response_content[l_index:r_index])
content = eval(response_content[l_index:r_index])
index_list = len(content)
print(content[index_list-1])
# print(binascii.b2a_hex('汉'.encode('utf-8')))
s = binascii.b2a_hex(u'汉'.encode('utf-8'))
# 进行解码，否则默认加上b,表示进行bytes进行输出
print(s.decode('utf-8'))


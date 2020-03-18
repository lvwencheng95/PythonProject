# -*- coding: utf-8 -*-
# @Time : 2020/3/17 14:08
# @Author : 52595
# @File : youxiangRegist.py
# @Python Version : 3.7.4
# @Software: PyCharm

# 获取完成，存放在字典中
# 本地读取内容
import json

import openpyxl
import requests
"""
功能描述：
    判断输入的网易邮箱是否已被注册.
    
注意事项：
"""


# 读取excel中文件
# 读取Excel中内容，参数1：excel中的路径；参数2：具体工作表(sheet)
def read_excel_xlsx(path, sheet_name):
    xlsx_list = list()
    workbook = openpyxl.load_workbook(path)
    # sheet = wb.get_sheet_by_name(sheet_name)这种方式已经弃用，不建议使用
    sheet = workbook[sheet_name]
    # 对行进行循环
    for row in sheet.rows:
        # 对某行的列进行循环
        for cell in row:
            xlsx_list.append(cell.value)
    return xlsx_list


# 存放内容，使用字典，key-value，value中的值为list
dic = dict()
cooky = 'JSESSIONID=0FB8AD2E88C9E9B1EB0135B4D1F6137B; MAIL_PINFO=lv_wen_cheng@163.com|1584423984|0|mail163|00&99|hub&1584409691&mail163#hub&421100#10#0#0|&0|urs&mail163|lv_wen_cheng@163.com; mail_psc_fingerprint=a0d8a088d38f6f166364f339f60977c7; _ntes_nnid=ab31b6f371d4299e3a1cf215d76d6fba,1563113519198; _ntes_nuid=ab31b6f371d4299e3a1cf215d76d6fba; usertrack=ezq0J10vwD0dshhUCZYCAg==; vinfo_n_f_l_n3=3c9bb31b9d4dd5ff.1.4.1567778441178.1579667239378.1579852975226; smslogin_trust="gj37f6s7tJgjqvLzVrWC+viBge7eKbhs8Elcq97Y6yWwTQHu5f0K1hTSSjRbpck2zk6GBGKF3QpN9nXGF0QOwo+YRxYlCq7YDM4O6nXkSzLMmbCVNfcuBcg2EBSIwrlGJcNVtY4lz9tA9pcaxz1lrYnHmHTOLh7/EacN3aBCNr4="; nts_mail_user=l_wencheng@163.com:-1:1; mailsync=87cf5d607d27e378125d2b3d87b6ce31b0aff565b41dca19b826f1db3bdb5758ab8bcd08c1e8b124a8dc42bce97830b5; ser_adapter=INTERNAL72; P_INFO=lv_wen_cheng@163.com|1584423984|0|mail163|00&99|hub&1584409691&mail163#hub&421100#10#0#0|&0|urs&mail163|lv_wen_cheng@163.com; mail_upx=t1bj.mail.163.com|t2bj.mail.163.com|t3bj.mail.163.com|t4bj.mail.163.com|t4bj.mail.163.com|t1bj.mail.163.com|t2bj.mail.163.com|t3bj.mail.163.com; mail_upx_nf=; mail_idc=; Coremail=b1489495da02c%yAdhaDlllPqwGokUKillbUQplxwqOMqD%g6a47.mail.163.com; MAIL_MISC=lv_wen_cheng; cm_last_info=dT1sdl93ZW5fY2hlbmclNDAxNjMuY29tJmQ9aHR0cHMlM0ElMkYlMkZtYWlsLjE2My5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRHlBZGhhRGxsbFBxd0dva1VLaWxsYlVRcGx4d3FPTXFEJnM9eUFkaGFEbGxsUHF3R29rVUtpbGxiVVFwbHh3cU9NcUQmaD1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNEeUFkaGFEbGxsUHF3R29rVUtpbGxiVVFwbHh3cU9NcUQmdz1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSZsPS0xJnQ9NyZhcz10cnVl; MAIL_SINFO=1584423984|0|3&80##|lv_wen_cheng; secu_info=1; mail_entry_sess=34b91ed292a89452fc8c77cbd1900d677f183d78196c04071bf06709dc12e348bef7c695b2311d809192b17c25124d48967c79a3647e6715b14116f75fb80fd03ba81ecb60cf1c131dc6e77ccf7cc1184a2b1f4c5d8362c702291903d5a2d1364d68a5fd3b1b8d6488dd9eca683559e154e8cfa2b424e380817e6b0cdc4228fdd710039a9950189ec69045a59abd7665c07193ebd294a08b69226680cd738f93f3e26cda725f1656b22f60bfcc0d24855a8b72c87fd3145306313e16c63b3d8e; mail_style=js6; mail_uid=lv_wen_cheng@163.com; mail_host=mail.163.com; ntes_misc=0||10#0|0|000020|0|mail163|'
header = {
    'Cookie': cooky,
    'Host': 'reg.mail.163.com',
    "Connection": "keep-alive",
    "X-Requested-With": "XMLHttpRequest",
    'Referer': 'https://reg.mail.163.com/unireg/call.do?cmd=register.entrance'
    # Firefox表示火狐
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    # Chrome表示谷歌
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
url_query = 'https://reg.mail.163.com/unireg/call.do?cmd=urs.checkName'
mailNameList = read_excel_xlsx('E:\\123456.xlsx', 'Sheet1')
if len(mailNameList) < 1:
    print('excel中不存在内容')
    exit(1)
# mailNameList = ['lvwencheng', 'limengjun', 'chenshuting', 'huxiao', 'chengongxu', 'zhuqiping']
list = list()
for mailNameTep in mailNameList:
    list.clear()
    mailName = mailNameTep
    # 表单提交中的参数
    params = {
        'name': mailName
    }
    # 好好去了解下pyhton中的request方法
    response = requests.get(url_query, headers=header, params=params)
    html = json.loads(response.content)
    if 'result' in html:
        # print(html['result'])
        if 'yeah.net' in html['result']:
            list.append('yeah.net')
        if '126.com' in html['result']:
            list.append('126.com')
        if '163.com' in html['result']:
            list.append('163.com')
    if len(list) > 0:
        dic[mailName] = list.copy()
'''
    if len(list) < 1:
        list.append('无')
    # 很奇怪，如果没有使用copy，则list中第二次的值会改变第一次的值
    dic[mailName] = list.copy()
'''
print(dic)
print('完成查询')

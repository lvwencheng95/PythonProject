# -*- coding: utf-8 -*-
# @Time : 2019/12/24 17:04
# @Author : 52595
# @File : 20191224_4.py
# @Software: PyCharm
import zipfile  # 导入模块，它是做压缩和解压缩的


zfile = zipfile.ZipFile("123456.zip")
passFile = open('pwd.txt')  # 读取你设定的密码文件

for line in passFile.readlines():
    try:
        password = line.strip('\n')
        zfile.extractall(path='D:\\developmentSoft\\pythonWorkspace\\', members=zfile.namelist(),
                         pwd=password.encode('utf-8'))
        # 若密码不正确，则直接抛异常，不执行下述代码
        print(password, "密码正确")
        break
    except:
        print(password, "密码错误")

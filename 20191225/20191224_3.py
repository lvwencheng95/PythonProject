# -*- coding: utf-8 -*-
# @Time : 2019/12/24 17:04
# @Author : 52595
# @File : 20191224_3.py
# @Software: PyCharm
import zipfile  # 导入模块，它是做压缩和解压缩的

password = "123"  # 我们设定的口令
zfile123456 = zipfile.ZipFile("123456.zip")  # 要解压缩的压缩包

# path为输出路径，即加压文件的输出位置
zfile123456.extractall(path='D:\\developmentSoft\\pythonWorkspace\\', members=zfile123456.namelist(),
                       pwd=password.encode('utf-8'))

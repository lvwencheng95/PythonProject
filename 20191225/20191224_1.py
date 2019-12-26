# -*- encoding:utf-8 -*-
# ---------定义一个列表，返回斐波那契数列的中值--------------------------#
# import test_20191224_1

# 方法1：使用import后，注意调用函数时，也要加上引入的文件名称
# outputData1 = test_20191224_1.f1(30)
# 方法2：
from test_20191224_1 import f1
outputData1 = f1(30)
print(outputData1)
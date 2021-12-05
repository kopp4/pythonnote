# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 22:48
# @Author  : taltalasuka
# @File    : graph.py
# @Software: PyCharm

import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas


data = pandas.read_csv("data.csv", encoding = "ANSI", header = None)
data = numpy.array(data)

print(data)

plt.bar(data[:,1], data[:,0])
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()


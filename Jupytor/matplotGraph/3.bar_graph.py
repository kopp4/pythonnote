# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 18:41
# @Author  : taltalasuka
# @File    : 3.bar_graph.py
# @Software: PyCharm

from matplotlib import pyplot as plt

x1 = [1, 3, 5, 7, 9]  # x1轴坐标数据
y1 = [5, 2, 7, 8, 2]  # y1轴坐标数据
x2 = [2, 4, 6, 8, 10]  # x2轴坐标数据
y2 = [8, 6, 2, 5, 6]  # y2轴坐标数据

plt.bar(x1, y1, label = "bar1")
plt.bar(x2, y2, label = "bar2")

plt.xlabel("bar")
plt.ylabel("barr")

plt.title("barbar")

plt.legend()

plt.show()
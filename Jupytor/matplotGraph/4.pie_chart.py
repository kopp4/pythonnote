# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 18:45
# @Author  : taltalasuka
# @File    : 4.pie_chart.py
# @Software: PyCharm

from matplotlib import pyplot as plt

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']

slice = [9, 9, 5, 5, 1]
slice_name = ["benkyou", "nemuri", "gohan", "ge-mu", "unnko"]
colors = ["g", "y", "r", "m"]

plt.title("ore")

plt.pie(slice, labels = slice_name, colors = colors, explode = (0, 0.2, 0, 0, 0.5), shadow = True,)  # **labels** = slice_name

plt.show()

# help(plt.pie)

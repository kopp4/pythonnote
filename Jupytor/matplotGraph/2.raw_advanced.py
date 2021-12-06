# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 18:22
# @Author  : taltalasuka
# @File    : 2.raw_advanced.py
# @Software: PyCharm

from matplotlib import pyplot as plt

x = [1, 2, 4, 5]  # x轴坐标数据
y = [7, 8, 9, 10]  # y轴坐标数据

plt.rcParams["font.family"] = ["SimHei"] # CN font

plt.plot(x, y, "g", label = "rejoicing", lw = "3")
plt.plot(y, x, "b", label = "none", lw = "1", ls = ":", animated = False)

plt.title("candy - rejoice")

plt.xlabel("candy/g")
plt.ylabel("rejoice/L")

plt.legend()

# plt.savefig("graph", dpi = 99)

plt.show()
# help(plt.plot)



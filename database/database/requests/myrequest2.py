# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 19:02
# @Author  : taltalasuka
# @File    : myrequest2.py
# @Software: PyCharm

import requests

url = 'http://c.biancheng.net/uploads/course/python_spider/191009.html'

res = requests.get(url)

res.encoding = "utf-8"

print(res.text)

file = open("wrestling.txt", 'a+')

file.write(res.text)

file.close()

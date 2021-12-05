# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 18:59
# @Author  : taltalasuka
# @File    : myrequest.py
# @Software: PyCharm

import requests
# 引入 requests，实现请求

URL = 'http://c.biancheng.net/uploads/course/python_spider/191009.html'
# 输入在浏览器的网址

res = requests.get(URL)
# 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
# 答第二个问题，get() 方法需要输入一个网页链接

res.encoding = "utf-8"

print(res.text)
# 是时候回答第三个问题了，通过 type 查看返回的数据是什么对象。
# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 19:05
# @Author  : taltalasuka
# @File    : 3requestsphoto.py
# @Software: PyCharm

import requests

URL = 'http://rakuten-point.com/wp-content/uploads/RADWIMPS-%E4%BA%BA%E9%96%93%E9%96%8B%E8%8A%B1-%E5%88%9D%E5%9B%9E%E9%99%90%E5%AE%9A%E7%9B%A4-DVD%E4%BB%98-1.jpg'

res = requests.get(URL)

photo = open("eat_this.jpg", "wb")

photo.write(res.content)

photo.close()
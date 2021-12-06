# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 20:38
# @Author  : taltalasuka
# @File    : crawl.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

regex = r'''"volume":(\d+)[\s\S]*?"name":"(.+?)"'''

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# soup = BeautifulSoup(content, "html.parser")

file = "data.csv"

f = open(file, "w+")

for page in range(4):      # literal

    url = f"https://xueqiu.com/service/v5/stock/screener/quote/list?page={page + 1}&size=30&order=desc&order_by=volume&exchange=CN&market=CN&type=sha&_=1638709884497"

    fetching = requests.get(url, headers=HEADERS)

    content = fetching.text

    stock_name = re.findall(regex, content)

    for i, j in stock_name:
        print("成交量:" + i + "￥", j)
        f.write(i + ", ")
        f.write(j + "\n")

f.close()
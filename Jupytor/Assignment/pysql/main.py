# -*- coding: utf-8 -*-
# @Time    : 2021/11/21 19:10
# @Author  : taltalasuka
# @File    : main.py
# @Software: PyCharm

import pymysql

db = pymysql.onnect(host = "localhost",
                     user = "root",
                     password = "123456",
                     database = "CNdb", )

sql = "select * from student"

cur = db.cursor()

try:
    cur.execute(sql)

    data = cur.fetchall()

    for row in data:
        print("|SNo : {0} |SN : {1} |Sex : {2} |Age : {3}".format(row[0], row[1], row[2], row[3]))

finally:
    db.close()
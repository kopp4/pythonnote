# -*- coding: utf-8 -*-
# @Time    : 2021/11/14 15:36
# @Author  : taltalasuka
# @File    : 2_search_example.py
# @Software: PyCharm

import pymysql

sql = "select * from test"
# sql = "INSERT INTO test VALUES (2, 2, 2, 2, 2, 2, 2)"

db = pymysql.connect(host = "localhost",
                     user = "root",
                     password = "123456",
                     database = "hellomysql", )

cur = db.cursor()

try:
    cur.execute(sql)

    data = cur.fetchall()

    print(data)
    c = []
    for row in data:
        c.append(row[0])
        c.append(row[1])
        c.append(row[2])
        c.append(row[3])
        c.append(row[4])
        c.append(row[5])
        c.append(row[6])
    print(c)
    for i in c:
        print(i, end = " ")
    #     fname = row[0]
    #     lname = row[1]
    #     age = row[2]
    #     sex = row[3]
    #     income = row[4]
    #     test = row[5]

    db.commit()
except:
    print ("Error: unable to fetch data")
    db.rollback()

cur.close()
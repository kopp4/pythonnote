# -*- coding: utf-8 -*-
# @Time    : 2021/11/14 8:41
# @Author  : taltalasuka
# @File    : database1.py
# @Software: PyCharm

# python connect, create a database in mysql


'''
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

import pymysql

host = "localhost"
user = "root"
password = "123456"

# sql = "create database netease"
sql = "select version()"

db = pymysql.connect(host = host,
                     user = user,
                     password = password,
                     )
# create a *cursor*
cur = db.cursor()
try:
    # execute
    cur.execute(sql)

    data = cur.fetchone()
    print("database version : %s"  %data)
    # commit changes
    db.commit()
except:
    # if error rollback
    db.rollback()
# close the connection
db.close()
# -*- coding: utf-8 -*-
# @Time    : 2021/11/21 20:00
# @Author  : taltalasuka
# @File    : main2.py
# @Software: PyCharm

import pymysql

db = pymysql.connect(host = "localhost",
                     user = "root",
                     password = "123456",
                     database = "cndb",
                     charset = 'utf8')

sql = """
/* delete from student where SNo = (select max(SNO) as max_SNo from student)*/

delete from cndb.student order by SNo desc limit 1;


"""

cur = db.cursor()

try:
    cur.execute(sql)

    db.commit() # bruh

    print("Inserted!")
    data = cur.fetchall()

    for row in data:
        print("|SNo : {0} |SN : {1} |Sex : {2} |Age : {3}|".format(row[0], row[1], row[2], row[3]))

except:
    print("execute failed!")

finally:
    cur.close()
    db.close()
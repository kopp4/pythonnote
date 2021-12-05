#导入SQLite驱动：
import sqlite3
#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建：
conn=sqlite3.connect('test.db')
#创建一个Cursor：
cursor=conn.cursor()

#执行一条SQL语句，创建user表：
cursor.execute('create table user3 (id INTEGER PRIMARY KEY,name varchar(20))')
#通过rowcount获得插入的行数：
print(cursor.rowcount)   #1

cursor.execute("insert into user3 (name) values ('xmj')")
cursor.execute("insert into user3 (name) values ('yoyo')")
cursor.execute("insert into user3 (name) values ('lili')")

#关闭Cursor:
cursor.close()
#提交事务：
conn.commit()
#关闭Connection：
conn.close()


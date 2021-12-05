#导入SQLite驱动：
import sqlite3
#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建：
conn=sqlite3.connect('test.db')
#创建一个Cursor：
cursor=conn.cursor()
a='008'
b='John'
#继续执行一条SQL语句，插入一条记录：
cursor.execute("insert into user (id,name,password) values ('007','lilin','111')")
cursor.execute("insert into user (id,name,password) values (?,?,'222')",(a,b))
#通过rowcount获得插入的行数：
print(cursor.rowcount)   #1

#关闭Cursor:
cursor.close()
#提交事务：
conn.commit()
#关闭Connection：
conn.close()

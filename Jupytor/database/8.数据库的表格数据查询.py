#导入SQLite驱动：
import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()

#执行查询语句：
cursor.execute('select name from user')


#获得查询结果集：
values=cursor.fetchall()
print(values)   #[('Michael')]


for i in values:
    print(i[0])
    if i[0] == 'yoyo':
        print('yes')

cursor.close()
conn.close()

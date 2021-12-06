#coding:gb2312
#实例8-22：gui8_22.pyw
import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
from tkinter import *
fup=Frame()							#第一个框架用于放输入组件和对应的提示标签
fup.pack()

username=StringVar()					#用于绑定用户名输入组件
password=StringVar()					#用于绑定密码输入组件

def usercheck(what):
    if len(what)>10:
        label3.config(text='用户名不能超过10个字符',fg='red')
        return False
    return True
def passwordcheck(why,what):
    if why=='1':
        if what not in '0123456789':
            label3.config(text='密码只能是数字',fg='red')
            return False
    return True
def clear():
    entry1.delete(0,END)
    password.set('')
    label3.config(text='')
def build():
    fnew.destroy()
    f1 = Frame()  # 第一个框架用于放输入组件和对应的提示标签
    f1.pack()
    Label(f1, text='查询的商品名称：', anchor=E).grid(row=1, column=1)
    shangping_id = StringVar()
    spid = Entry(f1, textvariable=shangping_id)
    spid.grid(row=1, column=2)
    Label(f1, text='显示商品价格：', anchor=E).grid(row=1, column=3)
    shangping_price = StringVar()
    spprice = Entry(f1, textvariable=shangping_price)
    spprice.grid(row=1, column=4)
    Button(f1, text='查询', anchor=E).grid(row=1, column=5)

    Label(f1, text='输入商品名称：', anchor=E).grid(row=2, column=1)
    shurusp_id = StringVar()
    srspid = Entry(f1, textvariable=shurusp_id)
    srspid.grid(row=2, column=2)
    Label(f1, text='输入调整价格：', anchor=E).grid(row=2, column=3)
    tiaozheng_price = StringVar()
    tzprice = Entry(f1, textvariable=tiaozheng_price)
    tzprice.grid(row=2, column=4)
    Button(f1, text='修改', anchor=E).grid(row=2, column=5)

    Label(f1, text='输入新增商品名称：', anchor=E).grid(row=3, column=1)
    xinzengsp_id = StringVar()
    xzspid = Entry(f1, textvariable=xinzengsp_id)
    xzspid.grid(row=3, column=2)
    Label(f1, text='输入商品价格：', anchor=E).grid(row=3, column=3)
    xz_price = StringVar()
    xzprice = Entry(f1, textvariable=xz_price)
    xzprice.grid(row=3, column=4)
    Button(f1, text='添加', anchor=E).grid(row=3, column=5)


def new():
    global fnew
    fnew = Frame()  # 第一个框架用于放输入组件和对应的提示标签
    fnew.pack()
    bt3 = Button(fnew, text='新建',command=build)
    bt3.grid(row=1, column=1)


def sett():
    # 执行查询语句：
    cursor.execute('select name from user')
    # 获得查询结果集：
    values = cursor.fetchall()
    c=[]
    for i in values:
        c.append(i[0])
    print(c)
    a=username.get()
    b=password.get()
    if a in c:
        cursor.execute('select password from user where name="%s"'%a)
        ps=cursor.fetchall()
        print(ps[0][0])
        if b==ps[0][0]:
            label3.config(text='登录成功，用户名为%s,密码为%s' % (a, b), fg='red')
            fup.destroy()
            fdown.destroy()
            label3.destroy()
            new()

        else:
            label3.config(text='密码错误', fg='red')

    else:
        label3.config(text='用户名错误', fg='red')






label1=Label(fup,text='用户名：',width=8,anchor=E)
label1.grid(row=1,column=1)
entry1=Entry(fup,textvariable=username,width=20)			#用户名输入组件
docheck1=entry1.register(usercheck)#自带验证功能，usercheck自定义函数
entry1.config(validate='all',validatecommand=(docheck1,'%P'))
entry1.grid(row=1,column=2)

label2=Label(fup,text='密码：',width=8,anchor=E)	
label2.grid(row=2,column=1)
entry2=Entry(fup,show='*',textvariable=password,width=20) 	#密码输入组件
docheck2=entry2.register(passwordcheck)
entry2.config(validate='all',validatecommand=(docheck2,'%d','%S'))
entry2.grid(row=2,column=2)

fdown=Frame()
fdown.pack()
bt1=Button(fdown,text='重置',command=clear)
bt1.grid(row=1,column=1)

bt2=Button(fdown,text='确定',command=sett)
bt2.grid(row=1,column=2)

# fup.destroy()
# label2.destroy()
# label1.destroy()
# fdown.destroy()

label3=Label()
label3.pack()
mainloop()

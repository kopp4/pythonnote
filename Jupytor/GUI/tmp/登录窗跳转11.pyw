#coding:gb2312
#ʵ��8-22��gui8_22.pyw
import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
from tkinter import *
fup=Frame()							#��һ��������ڷ���������Ͷ�Ӧ����ʾ��ǩ
fup.pack()

username=StringVar()					#���ڰ��û����������
password=StringVar()					#���ڰ������������

def usercheck(what):
    if len(what)>10:
        label3.config(text='�û������ܳ���10���ַ�',fg='red')
        return False
    return True
def passwordcheck(why,what):
    if why=='1':
        if what not in '0123456789':
            label3.config(text='����ֻ��������',fg='red')
            return False
    return True
def clear():
    entry1.delete(0,END)
    password.set('')
    label3.config(text='')
def build():
    fnew.destroy()
    f1 = Frame()  # ��һ��������ڷ���������Ͷ�Ӧ����ʾ��ǩ
    f1.pack()
    Label(f1, text='��ѯ����Ʒ���ƣ�', anchor=E).grid(row=1, column=1)
    shangping_id = StringVar()
    spid = Entry(f1, textvariable=shangping_id)
    spid.grid(row=1, column=2)
    Label(f1, text='��ʾ��Ʒ�۸�', anchor=E).grid(row=1, column=3)
    shangping_price = StringVar()
    spprice = Entry(f1, textvariable=shangping_price)
    spprice.grid(row=1, column=4)
    Button(f1, text='��ѯ', anchor=E).grid(row=1, column=5)

    Label(f1, text='������Ʒ���ƣ�', anchor=E).grid(row=2, column=1)
    shurusp_id = StringVar()
    srspid = Entry(f1, textvariable=shurusp_id)
    srspid.grid(row=2, column=2)
    Label(f1, text='��������۸�', anchor=E).grid(row=2, column=3)
    tiaozheng_price = StringVar()
    tzprice = Entry(f1, textvariable=tiaozheng_price)
    tzprice.grid(row=2, column=4)
    Button(f1, text='�޸�', anchor=E).grid(row=2, column=5)

    Label(f1, text='����������Ʒ���ƣ�', anchor=E).grid(row=3, column=1)
    xinzengsp_id = StringVar()
    xzspid = Entry(f1, textvariable=xinzengsp_id)
    xzspid.grid(row=3, column=2)
    Label(f1, text='������Ʒ�۸�', anchor=E).grid(row=3, column=3)
    xz_price = StringVar()
    xzprice = Entry(f1, textvariable=xz_price)
    xzprice.grid(row=3, column=4)
    Button(f1, text='���', anchor=E).grid(row=3, column=5)


def new():
    global fnew
    fnew = Frame()  # ��һ��������ڷ���������Ͷ�Ӧ����ʾ��ǩ
    fnew.pack()
    bt3 = Button(fnew, text='�½�',command=build)
    bt3.grid(row=1, column=1)


def sett():
    # ִ�в�ѯ��䣺
    cursor.execute('select name from user')
    # ��ò�ѯ�������
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
            label3.config(text='��¼�ɹ����û���Ϊ%s,����Ϊ%s' % (a, b), fg='red')
            fup.destroy()
            fdown.destroy()
            label3.destroy()
            new()

        else:
            label3.config(text='�������', fg='red')

    else:
        label3.config(text='�û�������', fg='red')






label1=Label(fup,text='�û�����',width=8,anchor=E)
label1.grid(row=1,column=1)
entry1=Entry(fup,textvariable=username,width=20)			#�û����������
docheck1=entry1.register(usercheck)#�Դ���֤���ܣ�usercheck�Զ��庯��
entry1.config(validate='all',validatecommand=(docheck1,'%P'))
entry1.grid(row=1,column=2)

label2=Label(fup,text='���룺',width=8,anchor=E)	
label2.grid(row=2,column=1)
entry2=Entry(fup,show='*',textvariable=password,width=20) 	#�����������
docheck2=entry2.register(passwordcheck)
entry2.config(validate='all',validatecommand=(docheck2,'%d','%S'))
entry2.grid(row=2,column=2)

fdown=Frame()
fdown.pack()
bt1=Button(fdown,text='����',command=clear)
bt1.grid(row=1,column=1)

bt2=Button(fdown,text='ȷ��',command=sett)
bt2.grid(row=1,column=2)

# fup.destroy()
# label2.destroy()
# label1.destroy()
# fdown.destroy()

label3=Label()
label3.pack()
mainloop()

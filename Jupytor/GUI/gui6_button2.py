# coding:utf-8

from tkinter import *

top = Tk()
top.title(u"主窗口")
bt1 = Button(top,text=u"禁用",state=DISABLED)  # 将按钮设置为禁用状态
bt2 = Button(top,text=u"退出",command=top.quit)  # 设置回调函数
bt1.pack(side=LEFT)
bt2.pack(side=LEFT)
top.mainloop()
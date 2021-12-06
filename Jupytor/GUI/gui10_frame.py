# coding:utf-8

from tkinter import *

top = Tk()
top.title(u"主窗口")
for relief_setting in ["raised", "flat", "groove", "ridge", "solid", "sunken"]:
    frame = Frame(top, borderwidth=2, relief=relief_setting)  # 定义框架
    Label(frame, text=relief_setting, width=10).pack()
    # 显示框架，并设定向左排列，左右、上下间隔距离均为5像素
    frame.pack(side=LEFT, padx=5, pady=5)
top.mainloop()

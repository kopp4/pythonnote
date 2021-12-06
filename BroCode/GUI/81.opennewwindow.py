# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 23:00
# @Author  : taltalasuka
# @File    : 81.opennewwindow.py
# @Software: PyCharm

from tkinter import *

def create_window():
    new_window = Toplevel()
    # new_window = Tk()


window = Tk()

Button(window, text = "create new windows", command = create_window).pack()

window.mainloop()
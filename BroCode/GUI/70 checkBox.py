# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 22:36
# @Author  : taltalasuka
# @File    : 70 checkBox.py
# @Software: PyCharm
import src


from tkinter import *



def display():
    if(x.get() == 1):
        print("u agree")
    else:
        print("u dont agree")


window = Tk()

phote = PhotoImage(file ="src/ave.gif")

x = IntVar()        # between Tk and check_button
# x = BooleanVar()
# offvalue = false
# on value = true

check_button = Checkbutton(window, text = "bruh",
                           variable = x,
                           onvalue = 1,
                           offvalue = 0,
                           command = display,
                           fg = "#00FF00",
                           bg = "black",
                           activeforeground = "#00FF00",
                           activebackground = "black",
                           image = phote, compound = "left", )
check_button.pack()
window.mainloop()
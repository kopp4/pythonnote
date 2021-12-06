# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 22:49
# @Author  : taltalasuka
# @File    : 71.radiobuttons.py
# @Software: PyCharm

from tkinter import *
import src
food = ["pizza", "hamburger", "hotdog"]




window = Tk()

x = IntVar()

image = PhotoImage(file = "src/ave.gif")

foodImage = [image, image, image]

for index in range(len(food)):
    radiobutton = Radiobutton(window, text = food[index],
                              variable = x,
                              value = index,
                              padx = 25,
                              image = foodImage[index],
                              compound = "left",
                              indicator = 0,


                              )
    # radiobutton.config
    radiobutton.pack(anchor = W)
window.mainloop()
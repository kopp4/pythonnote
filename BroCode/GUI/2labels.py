# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 17:35
# @Author  : taltalasuka
# @File    : 2labels.py
# @Software: PyCharm

from tkinter import *   # bruh don't

window = Tk()

photo = PhotoImage(file ="src/ave.gif")    # double slash **gif** only

label = Label(window, text = "Hello asuka, do you even laugh",
              font = ("Arial", 40, "underline"),
              fg = "#00FF00", bg = "#2B2B2B",
              relief = RAISED,
              bd = 10,
              padx = 100,
              pady = 200,
              image = photo,
              compound = "top"   # direction where the image is placed
            )
                # Every value is label not the literal "background"
# label.place(x = 0, y = 0)   # put the widget in the window
#   ^
#   |
#   v
label.pack()    # put the widget in the window


window.mainloop()
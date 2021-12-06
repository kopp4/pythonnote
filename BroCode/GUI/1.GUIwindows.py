# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 17:04
# @Author  : taltalasuka
# @File    : 1.GUIwindows.py
# @Software: PyCharm

from tkinter import *# u should not do this next time

# widgets : GUi elements: buttons, textboxes, labels, images
# windows : servers as a container to hold the widgets contain these windows

window = Tk()
window.geometry("1080x1920")
window.title("taltalasuka")
window.config(background = "#2b2b2b")

icon = PhotoImage(file ="src/ave.gif")
window.iconphoto(True, icon)

window.mainloop()

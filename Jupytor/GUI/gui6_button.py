# 创建一个按钮，单击按钮的时候，在屏幕中打印出信息。用到command参数。
from tkinter import *


def happy():  # 创建回调函数
    print("恭喜你获得100万！！！")


root = Tk()
root.geometry("300x300")
button = Button(root, text="抽奖", command=happy)  # 创建Button组件,单击按钮的时候调用回调函数
button.pack()
root.mainloop()

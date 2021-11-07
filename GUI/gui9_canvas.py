# Canvas组件称为画布组件，可以用Canvas类来绘制图形元素，例如线条、圆形、正方形等。
from tkinter import *

root = Tk()
root.title("画直线")
root.geometry("300x300")
# 创建Canvas组件的对象canvas，并指定画布的长度、高度和背景色。
canvas = Canvas(root, width=200, height=200, bg="yellow")
# 画直线，4个参数分别是起点的坐标和终点的坐标
canvas.create_line(0, 0, 100, 100)
# 画矩形
canvas.create_rectangle(120,120,180,180,fill="blue")
canvas.pack()
root.mainloop()

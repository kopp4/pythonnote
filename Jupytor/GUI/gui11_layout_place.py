"""
3.place布局管理方式
place布局可以显式地指定组件的绝对位置或者相对于其他组件的位置。
使用方法：组件对象.place()
比较重要的属性有:
x、y：绝对位置坐标。
width、height：组件的宽度和高度。
relx、rely：组件相对于父容器的x、y坐标，值为0~1之间的浮点数。
relwidth、relheight：组件相对于父容器的宽度和高度。
"""
from tkinter import *

root = Tk()
root.geometry("300x400")
label_1 = Label(root, text="绝对位置", bg="green")
label_1.place(x=150,y=180)

label_2 = Label(root, text="相对坐标位置", bg="red")
label_2.place(relx=0.5,rely=0.5)

label_3 = Label(root, text="相对宽度和高度位置", bg="blue")
label_3.place(relwidth=0.5,relheight=0.5)
root.mainloop()

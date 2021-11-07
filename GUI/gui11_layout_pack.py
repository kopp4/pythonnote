"""
在tkinter中，有3种组件布局管理方式，分别为pack,grid,place。
1.pack布局
pack是指定相对位置的布局方式，在不要求精确布局的场景下可以使用。
pack布局默认按照放置的先后顺序从上到下排列，pack会为组件指定合适的位置和大小。
pack有几个比较重要的参数，分别是side,fill,padding。
side：指定组件依次靠窗口排放的位置。有：left,right,top,bottom。
fill：指定组件的填充方式。有：X,Y,BOTH,NONE。X：组件在水平方向进行填充；……
padding：指定组件边距，主要有内边距、外边距、水平边距、垂直边距。有：padx,pady,ipadx,ipady。
"""
from tkinter import *

root = Tk()
root.geometry("200x200")
root.title("组件排放位置")
label_1 = Label(root, text="one", bg="green")
label_1.pack(side="top")

label_2 = Label(root, text="two", bg="red")
label_2.pack(side="top",fill=X,pady=10)

label_3 = Label(root, text="three", bg="blue")
label_3.pack(side="top")
root.mainloop()

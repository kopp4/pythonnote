# 用Label组件来展示图片
import tkinter as tk
from tkinter import Tk as Baba # another life cheat

root = Baba()
root.geometry("519x563")  # 将根窗口的大小设置为图片的大小。图片大小可以查看图片属性的详细信息。
# 要展示的图片路径，两种表示法：
# pic = 'C:\\Users\\Public\\Pictures\\3.gif' #用双反斜杠
pic = 'D:\\pythonnote\\BroCode\\GUI\\ave.gif'
photo = tk.PhotoImage(file=pic)  # 通过PhotoImage类创建了一个图片对象，参数是图片的地址。
# 创建Label组件，并且设置要展示的图片
label = tk.Label(root, image=photo)
label.pack()
root.mainloop()

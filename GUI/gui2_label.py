# Label组件可以在根窗口中展示文字或者图片
import tkinter as tk  # 导入tkinter模块，为它取一个新名字，叫作tk

root = tk.Tk()  # tk.Tk()这个函数用于创建根窗口
root.geometry("320x240")  # 设置窗口大小，中间是字母x
root.title("我的Label")
label = tk.Label(root, text="Hello Python!", bg="pink")  # 创建label组件，设置文本，背景颜色
label.pack()  # 将Label添加到窗口。
# tkinter共有3种布局管理方式，分别是pack布局、grid布局、place布局。
root.mainloop()  # 让根窗口持续展示。如果组件有变化，它将会不断地刷新。

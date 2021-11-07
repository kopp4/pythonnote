# 使用PIL展示了tkinter不能展示的JPEG图片。
# PhotoImage类支持的图片格式是.gif。
# PIL(Python Imaging Library)是Python的第三方图像处理库。先安装pillow, pip3 install pillow。
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.geometry("1000x800")
path = '/BroCode/GUI/src/sayuri.jpg'  # 图片路径，用双反斜杠
image = Image.open(path)  # 打开图片

photo = ImageTk.PhotoImage(image)  # 创建tkinter兼容的图片

label = tk.Label(root, image=photo)  # 创建Label组件对象
label.pack()  # 展示Label对象
root.mainloop()  # 保持窗口展示

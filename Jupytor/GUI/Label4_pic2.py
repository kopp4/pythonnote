# Label既展示图片又展示文字
import tkinter as tk

root = tk.Tk()
root.geometry("519x600")
# 要展示的图片路径，有两种表示法：
# pic = 'C:\\Users\\Public\\Pictures\\3.gif' # 使用双反斜杠
pic = 'D:\\pythonnote\\BroCode\\GUI\\ave.gif'  # 使用/斜杠
photo = tk.PhotoImage(file=pic)  # 创建图片对象 gif only
str = "大家好，我是小邦学姐"
# 创建Label组件，并且设置要展示的图片
label = tk.Label(root, text=str, image=photo, compound="top", font=('黑体', 20))
# compound指示图像和文本的位置，top图像在文字的顶部，还有left、right、bottom、center。
label.pack()
root.mainloop()

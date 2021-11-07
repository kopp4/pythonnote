from tkinter import *

root = Tk()
root.geometry("300x400")
# 创建Label组件对象
label_account = Label(root, text="账号")
# 将label组件布局在第0行第0列
label_account.grid(row=0, column=0)

entry_account = Entry(root)  # 创建Entry组件的对象
# 将Entry组件布局在第0行第1列
entry_account.grid(row=0, column=1)

# 创建Label组件对象
label_pwd = Label(root, text="密码")
# 将label组件布局在第1行第0列
label_pwd.grid(row=1, column=0)

entry_pwd = Entry(root)  # 创建Entry组件的对象
# 将Entry组件布局在第1行第1列
entry_pwd.grid(row=1, column=1)
root.mainloop()
# 用Entry组件来做一个用户登录界面。
# Entry组件用来接收字符串输入，允许用户输入一行文字，如果想输入多行文字，则可以用Text组件。
from tkinter import *

root = Tk()
root.title("登录界面")

# 创建Label组件对象label_account
label_account = Label(root, text="账号")
# 将Label组件放到根窗口，靠左边排放
label_account.pack(side="left")

# 创建Entry组件对象entry_account
entry_account = Entry(root)
# 将Entry组件放到根窗口，靠左边排放
entry_account.pack(side="left")

# 创建Label组件对象label_pwd
label_pwd = Label(root, text="密码")
# 将Label组件放到根窗口，靠左边排放
label_pwd.pack(side="left")

# 创建Entry组件对象entry_pwd
entry_pwd = Entry(root)
# 将Entry组件放到根窗口，靠左边排放
entry_pwd.pack(side="left")
root.mainloop()

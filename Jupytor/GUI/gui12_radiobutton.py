from tkinter import *

top = Tk()
top.title(u"单选")
f1 = Frame(top)
choice = IntVar(f1)
for txt, val in [('1', 1), ('2', 2), ('3', 3)]:
    # 将所有的选项与变量choice绑定
    r = Radiobutton(f1, text=txt, value=val, variable=choice)
    r.pack()

choice.set(1)  # 设定默认选项
Label(f1, text="您选择了：").pack()
Label(f1, textvariable=choice).pack()  # 将标签与变量动态绑定
f1.pack()
top.mainloop()

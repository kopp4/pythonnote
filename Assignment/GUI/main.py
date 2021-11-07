import random
from tkinter import *



def show():

    window = Tk()

    label1 = Label(window, text = "账号")
    label2 = Label(window, text = "密码")
    label3 = Label(window, text = "验证码")
    label4 = Label(window, text = generateNum())

    entry1 = Entry(window)
    entry1.place(x = 40, y = 50)
    entry2 = Entry(window)
    entry2.place(x = 40, y = 100)
    entry3 = Entry(window)
    entry3.place(x = 40, y = 150)

    window.geometry("250x250")

    label1.place(x = 0, y = 50)
    label2.place(x = 0, y = 100)
    label3.place(x = 0, y = 150)
    label4.place(x = 180, y = 150)

    button = Button(window, text = "提交", command = complete)

    button.place(x = 100, y = 170)

    window.mainloop()

def generateNum():

    valid = []
    for i in range(6):
        valid.append(random.randint(0, 9))
    print(valid)
    return valid

def complete():
    print("Compelete!")


if __name__ == '__main__':
    show()

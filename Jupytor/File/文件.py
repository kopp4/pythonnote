import os
import shutil

path = "D:\\pythonnote\\Jupytor\\File\\test.txt"
dst = "D:\\pythonnote\\New Folder\\copiedtest.txt"
jpgpath = "D:\\pythonnote\\Jupytor\\File\\horny.jpg"

print("Executing in : " + os.getcwd())  # check the current dir
# or detectFile
def createFile():
    if os.path.exists(path):
        print("File is already in the dir")
    else:
        open(path, "a")
        print("File is created!")
# python reading a file in many ways
def readFile():
    #1.
    with open(path, encoding = "utf - 8") as file:
        print("\n1. :" + file.read())              # read all the content
    #2.                           #todo big file wasting time so dont use read
    with open(path, encoding = "utf - 8") as file:#fixme  file is closed
        print("\n2. :" + file.readline())          #fixme so we won't use this in the next func
    #3.
    with open(path, encoding = "utf - 8") as file:
        list = file.readlines() # returning a list BRUH!!!
        #3.1
        print("3.1. ", end = "")
        print(list)
        #3.2
        print("3.2. : readlines : ", end = "")
        print(*list, end = "")      #todo [*] 把列表变成参数
    #4.
    with open(path, encoding = "utf - 8") as file:
        print("\n4. : ", end = "")
        for line in file:
            print(line, end = "")

#python write a file
#1. write
#2. writelines
#3. flush : writing the file without closing it
def writeFile():

    file = open(path, "r+", encoding = "utf - 8") #todo without '+' cant read
    file.write("\nTrying to write")
    print("Done!")
    i = 1
    for line in file:
        print(str(i) + "th time try to write:")
        print(line, end = "")  # 文件中每一行本身有一个换行所以用end=""让print不换行
        i += 1
    file.close()
#python copy file
def copyFile():
    try:                        # might not that need of exception
        shutil.copyfile(path, dst)
        print("Successfully executed!")
    except FileNotFoundError:
        print("The file is not found :(")

    ##2.

#python move a file
def moveFile():
    try:
        if os.path.exists(dst):    # find ur dst bzc u got except to prevent error
            print("File is already created!")
        else:
            shutil.move(path, dst)
            print("File is successfully moved!")
    except FileNotFoundError:
        print("Oooooooooooooops! Not file is found. QQ")
#python copy a binary file such as pic or ...
def copybinaryFile():
    with open(jpgpath, "rb") as f:                      # todo  it is RB!!!!!!
        b = f.read()
        copy_f_name = "notanymore.jpg"
        with open(copy_f_name, "wb") as copy_f:         #todo it is WB!!!!
            copy_f.write(b)
            print("Done!wwww")

def eg4():
    # 例4 假设文件data.txt中有若干整数，
    # 所有整数之间使用英文逗号分隔，编写程序读取所有整数，
    # 将其按升序排序后再写入文本文件data_asc.txt中
    with open('../data.txt', 'r') as fp:
        data = fp.readlines()  # 读取所有行
    data = [line.strip() for line in data]  # 删除每行两侧的空白字符
    data = ','.join(data)  # 合并所有行
    print(data)
    data = data.split(',')  # 分隔得到所有数字字符串
    data = [int(item) for item in data]  # 转换为数字
    data.sort()  # 升序排序
    data = ','.join(map(str, data))  # 将结果转换为字符串
    with open('../data_asc.txt', 'w') as fp:  # 将结果写入文件
        fp.write(data)


if __name__ == "__main__":
    # createFile()
    # readFile()
    # writeFile()
    #copyFile()
    copybinaryFile()
    # moveFile()
    # eg4()
    #   Summary : Func is [file.x()]
    # todo : also, python func is all lowercase + "_"


#This "decent" amount of codes is driving Linbei CRAZY!!!!!
#   CURSE U!!!!!!!!!!!!!



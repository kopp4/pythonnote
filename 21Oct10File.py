# python detect a file
import os
import shutil
path = "D:\\pythonnote\\New Folder\\PORNPIC.jpg"
dst = "D:\\pythonnote\\porn.txt"
def createFile():
    if os.path.exists(path):
        print("File is already in the dir")
    else:
        open(path, "a")
        print("File is created!")
def detectFile():
    if os.path.exists(path):
        print("The file is found")
    else:
        open(path, 'a')

#pyhon copy file
def copyFile():
    try:                        # might not that need of exception
        shutil.copyfile(path, dst)
        print("Successfully executed!")
    except FileNotFoundError:
        print("The file is not found :(")

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
if __name__ == "__main__":
    # createFile()
        #==
    # detectFile()
    # copyFile()
    moveFile()

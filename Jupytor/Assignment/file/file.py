import datetime
import os

path = "demo.txt"
picpath = os.getcwd() + "\\pic"
dst = os.getcwd() + "\\newpicfolder"   #destination of the new pics

def userinpt():     # recording user input
    #creating file
    if os.path.exists(path):
        print("File is already created.")
    with open(path, "r+") as file:
        print(file.read())

def renamepic():    # rename pics in batch
    dir = os.listdir(picpath)
    count = 0
    for i in dir:
        with open(picpath + "\\" + dir[count], "rb") as file:
            tmp = file.read()

            altered_name = str(datetime.datetime.now())
            altered_name = altered_name[0:9] + str(count) + ".jpg"
            with open(dst + "\\" + altered_name, "wb") as copied_file:
                copied_file.write(tmp)
                count += 1
                print("The " + str(count) + "th file is copied")
        # with open(i, "rb") as file:
        #   tmp = file.read()
        #   print(tmp)
if __name__ == '__main__':
    # userinpt()
    renamepic()

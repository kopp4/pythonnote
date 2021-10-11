url = 'https://www.youtube.com/watch?v=XKHEtdqhLK8&ab_channel=BroCode'
#                                                  8. String Slicing
# [start:stop:step]

# name = 'Bro Code'
# first_name = name[:3]
# last_name = name[4:]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(reversed_name)
# #slice just the same without column
#
# website = 'http://google.com'
# slice = slice(7, -4)
# print(website[slice])

#                                                   14. loop control statement#
phone_number = '123-456-7890'
# for i in phone_number:
#     if i == '-':
#         continue
#     print(i, end = '')  # note that if u don wanna change the line u could type end = ''
#
# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i, end = ' ')

# age = input('Enter your age:')
#
#split method (from str to list)
# print(phone_number.split("-"))
#
# 16. 2D lists


# Using above first method to create a
# 2D array
# rows, cols = (5, 5)
# arr = [[0]*cols]*rows
# print(arr)
#
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
# food = [drinks, dinner, dessert]
# # print(food[0][1])
# print([rows for column in food for rows in column], end = "")                             # **ESSENTIAL**
#                   should've name them rows & columns
#
# 17. tuple
# student = ("Bro", 21, "male")
# print(student.count("Bro"))
# print(student.index("Bro"))
# for x in student:
#     print(x)
# if "Bro" in student:
#     print("Bro is in the tuple")
#
#
#18. set
# utensils = {"fork", "spoon", "knife"}
# for x in utensils:
#     print(x)                # everytime u print the set value is not ordered
#


# 19. dictionaries python





# try:
#     print('ur age is : ' + age)
#     if int(age) <= 0:
#         raise Exception("Age must be above 0")
# except Exception as e:
#     print(e)

#31.                                    file detection
#
#
# import os
# path = "D:\\pythonnote\\hellopython.txt"
# if os.path.exists(path):
#     print("location exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a diractory")
# else:
#     print("that location doesn't exist")
#
#
#32.                                python read a file
#
#
# with open("hellopython.txt") as file :      # close the file automatically for u
#     print(file.read())                      # but can't handling exception so we
#           ||
#           ||
#           \/
# try:
#     with open("hellopython.txt") as file :
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found :(")
#
#
#33.                    python write a file
#
#
# text = "\nYoooooooooooooooo\nThis is some text appending"
# with open("hellopython.txt", "a") as file: # overwrite the file : w
#     file.write(text)
#--------------------------------
#
#   "r" read
#   "w" overwrite
#   "x" write
#   "a" append
#   "b" binary
#   "t" text
#   "+" used with the method above like "w+" "r+" "a+"
#       meaning it is editable
#
#--------------------------------
#
#
#34.                     python copy a file
#
#
# import shutil
# shutil.copy("hellopython.txt", "D:\\pythonnote\\file.txt")  # source, distination(src, dst)
#
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a dir such as "D:\\pythonnote\\new folder"
# copy2() = copy() + copies metadata (file's creation and modification times)
#35.                move a file
#
#
# import os
# src = "hellopython.txt"   # U could move a dir too
# dst = "D:\\pythonnote\\New Folder\\movedfile.txt"
# try:
#     if os.path.exists(dst):
#         print("already a file")
#     else:
#         os.replace(src, dst)
#         print(src + " was moved")
# except FileNotFoundError:
#     print(src + " was not found")
#
#
#36.
#
#
# import os
# import shutil
# try:
#     os.remove("file.txt")
#
#     #print("The file is moved!")   best do it in the else
# except FileNotFoundError:
#     print("Ooops!There is no file exist")
# except PermissionError:
#     print("Bro u can't delete a dir im sry")    # can't delete a dir
# except OSError:
#     print("u cannt that file using that func")

#
#
#37.
#
#
#
#
#38.
#
#
#
#
#39.
#
#
#
#
#40.
#
#
#
#




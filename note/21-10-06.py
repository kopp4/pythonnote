# -*- coding:utf-8 -*-

#function嵌套
# def outer():
#     def inner():
#         print('this is inner function')
#     print('this is outer function')
#     inner()
#
# outer()
#
#
# def mul():
#     global tip  # make local variable global
#     tip = 'this is tip in function'
#     print(tip)
# tip = 'this is a globla tip'
# mul()
# print(tip)
#
#
# def func4():
#     e = 1 # essential
#     def inner():
#         nonlocal e # search for the nearest 'e' **above**
#         e = 'this is a nonlocal variable'
#         print(e)
#     inner()
#     print(e)
# e = 1
# func4()
# print(e)
#
#
#4TH Data Structure#
#1. Tuple#
import os

# tuple1 = (1, 3, 5, 7, 9)
#slice#
# print(tuple1[0:3])
# print(tuple1[0:5:2])
# print(tuple1[::-1])
# print(tuple1[-3:-1])
#search 'in'#
#
#
# if 3 in tuple1:
#     print('humanity just found a brand new element')
#
#
# print(max([111, 22, 3], key = str))
#
#
#
#   2. List #
# list1 = ['1', '2', '3', '4', '5']
# print(''.join(list1))
#   PS
#  enumerate
# seasons = ['spring', 'summer', 'fall', 'winter']
# for index, item in enumerate(seasons):
#     print(index, item)
# chars = 'python'
# for i, chr in enumerate(chars):
#     print(i, chr)
#
#
# 3.     Dict    #
# zergling = {'attack' : 5, 'speed' : 4.13, 'price' : 50}
# print(zergling)
# print(zergling['price'])
#                                   Error when printing zergling[0]
#                       * dict * is not orderer as I said before
# print(zergling.get('attack', 0))   # 'get' method is way more safer bcz it wont error if a inexist value
# print(zergling.get('attac'), 333)     # returing value "none"
# zergling['targets'] = 'ground'
# print(zergling)
# zergling.pop('attack')
# zergling.popitem()
# print(zergling)
# print(zergling.values())
# print(zergling.keys())
# for a in zergling.keys():
#     print(a, end = ' ')
# for a in zergling.values():
#     print(a, end = " ")
#                   nested loop in dict
#
# for a, b in zergling.items(): # key, value
#     print(a, b)
#
# #                   Traversing Key & Value
# #                   item method
#
# zergling.update({Germany})

#       dict
# game = "mminecraft"
# dict = {}
# dict1 = {}                      # debugging it and u'll know
# for i in game:
#     print(i, end = ' ')
#     dict[i] = dict.get(i, 0) + 1
#     dict1[i] = dict1.get(i, 1)
# print(dict)
# print(dict1)
#                   Exception
#
#
#
# try:
#     with open("file.txt") as file :
#         print(file.read())
# except FileNotFoundError :
#     print("The file is not found :(")



# message1 = "Global Variable"
# def myFunction():
#     message1 = "Local Variable"
#     print("\nINSIDE THE FUNCTION")  #Global variables are accessible inside a function
#     print (message1)    #Declaring a local variable
#     # print (message1)    #Calling the function
# myFunction()
# print("\nOUTSIDE THE FUNCTION")     #Global variables are accessible outside function
# print (message1)     #Local variables are NOT accessible outside function.




#If you run the program, you will get the output below.
# INSIDE THE FUNCTION
# Global Variable
# Local Variable
# OUTSIDE THE FUNCTION
# Global Variable
# NameError: name 'message2' is not defined

#1. nonlocal用法
#
# count = 1
#
# def myfunc1():
#   x = "Bill"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x
#
# print(myfunc1())

#nonlocal只能在封装函数中使用，在外部函数先进行声明，在内部函数进行nonlocal声明
# 这样在b()函数中的count与a()中的count是同一个变量。

#
#
#2.外部函数中变量声明为global
# count = 1

#       **https://blog.csdn.net/lxy210781/article/details/81139493**

# path = "file.txt"
#
# def readFile():
#     try:
#         with open(path):
#             print(os.read(path))
#     except FileNotFoundError:
#         print("your file is not found")
#
#
# if __name__ == "__main__":
#     readFile()
#     # WriteFile()

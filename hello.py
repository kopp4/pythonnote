#!/user/bin/env python3
# _*_ coding: utf-8 _*_
# # string = 'Hello World!'
# # print(string)
# # mojang = 123
# # minecraft = ['block', 'stone', 'mob', mojang]
# # # print(minecraft[0:3])   #get every before mojang
# # # del minecraft[3]
# # # print(minecraft)
# # # minecraft.append(mojang)
# # # print(minecraft)
# # # print(len(minecraft))
# # # print(len(minecraft + minecraft))
# # # print(minecraft + minecraft)
# # # print(minecraft * 10)
# # # for i in minecraft :
# # #     print(i)    # i is element, can't use it as numbers or
# # numstr = [1, 2, 3, 4, 6]
# # print(max(numstr))
# # print(min(numstr))
# # print(minecraft.count('block'))
# #
# # print(numstr.extend(minecraft))
# # print(numstr)
# # # so the return value of the method is none, but the method used it is extended
# # print(numstr.index('stone'))
# # print(numstr.pop())# and delete it            also 'numstr.remove() dont have any return '
# # print(numstr)
# # print(minecraft.reverse()) # so this is wrong,
# # print(minecraft) # And that's right, in a summary python got so many unreturned method
# # # numstr.sort()
# # print(minecraft)
# # print('staff that i am passionated in: ' + minecraft)
# # num = input('吃我老母几口: ')
# # print('吃你老母' + num + '口')
#
# # 1.------------------------------------------------------
# first_name = 'natalie'
# last_name = 'lucy'
# print(first_name + ' ' + last_name)
# print(first_name.upper() + ' ' + last_name.upper())
# print(first_name.title() + ' ' + last_name)
# # 2.------------------------------------------------------
# name = ' jack '
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())
#
# # 3.------------------------------------------------------
# s1 = 'uforbgood'
# print(s1[0] + s1[3] + s1[5:9])


# sum = 0
# for i in range(0, 101, 2):
#     sum += i
# print(sum)

# first = 1
# second = 2
# third = 3
# total = first + second \
#     + third
# print(total)


# # 3.------------------------------------------------------
# 练习：生成一个含有 0-100 中所有偶数的列表

# list = [1, 2, 3]
# list2 = [4, 5, 6]
# print(list)
# print(list + list2)
# name1 = ('一点水', '两点水', '三点水', '四点水', '五点水')
# print(name1)
# print('一点水' in name1)
# dict1 = {1 : 2, 2 : 3}
# print(dict1)
# dict1['sayuri'] = 'taltalasuka'
# dict1['sayuri'] = 'sayuri149cm'
# print(dict1)
# set1 = set(dict1)
# print(set1)
# tuple1 = (1,3,5,7,9)
# print(f'the second element is {tuple1[0]}')

#--------------------------------------
# u should really pay attention to the
# "continue" in a loop
# bcz theres no bracket in python
#--------------------------------------
# count = 1
# sum = 0
# while (count <= 100):
#     if ( count % 2 == 0):  # 双数时跳过输出
#         count = count + 1
#         continue
#     sum = sum + count
#     count = count + 1
# print(sum)
#
# This is the sum of odd nums below 100
#
#--------------------------------------
# def print_user_info( name , age , sex = '男' ):
#     # 打印用户信息
#     print('昵称：{}'.format(name) , end = ' ')
#     print('年龄：{}'.format(age) , end = ' ')
#     print('性别：{}'.format(sex))
#     return;
#
# # 调用 print_user_info 函数
#
# print_user_info( '两点水' , 18 , '女')
# print_user_info( '三点水' , 25 )

# sum = 0
# evenlist = []
# for i in range(100):
#     if(i % 2 == 0):
#         sum += i
#         continue
# print(sum)


#--------------------------------------

# 练习：生成一个含有 0-100 中所有偶数的列表

#--------------------------------------
# evenlist = []
# for i in range(100):
#     if(i % 2 == 0):
#         evenlist.append(i)
#         continue
# print(evenlist)


# dict1 = "Python is an interpreted language"
# count = 1
#
# for i in dict1:
#     if i == ' ':
#         count = count + 1
# print(count)
# count = 0
#
# for i in dict1:
#     if i == 'a':
#         count = count + 1
# print(count)
#
#
# dict = {}
# for i in dict1:
#     dict[i] = dict.get(i, 0) + 1
# print(dict)

import random
#----------------------------------------
str = []
for i in range(100):
    str.append(random.randint(0, 1))
print(str.count(1))
print(str.count(0))
#----------------------------------------
num = random.randint(0, 100)
while 1:
    guess = int(input("plz enter the num:"))
    if guess > num:
        print("too big")
    elif guess < num:
        print("too small")
    elif guess == num:
        break
print("correct")
#-----------validate ISBN code-----------#
ISBN = input("Enter ur ISBN string:")
ISBN = ISBN.split('-')
ISBN = "".join(ISBN)
sum = 0
for i in range(12):
    if(i % 2 == 0):
        sum += 3 * int(ISBN[i])
    else: sum += int(ISBN[i])
remainder = 10 - sum % 10
print(ISBN)
if remainder == int(ISBN[11]):
    print("correct!")
else:
    print("Oops!")
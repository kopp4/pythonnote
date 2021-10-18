# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 23:43
# @Author  : taltalasuka
# @File    : 类和对象.py
# @Software: PyCharm

class Animal(object):
    def __init__(self, age, sex, weight):   # this might equal to "this" in Java
        self.age = age
        self.sex = sex
        self.weight = weight
animal = Animal(2, 1, 10.0)

# print("age".format(animal.age))
# print("sex".format(animal.sex))
# print("weight".format(animal.weight))

# print(animal.age)
# print(animal.sex)
# print(animal.weight)



import math

class Circle(object):
    def __init__(self, radius):
        print("Space : " + str(math.pi * radius ** 2))
        print("Circumference : " + str(6.28 * radius))
if __name__ == '__main__':
    circle = Circle(int(input("Radius:")))




# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 23:43
# @Author  : taltalasuka
# @File    : 类和对象.py
# @Software: PyCharm

# class Animal(object):
#     def __init__(self, age, sex, weight):   # this might equal to "this" in Java
#         self.age = age
#         self.sex = sex
#         self.weight = weight
# animal = Animal(2, 1, 10.0)

# print("age".format(animal.age))
# print("sex".format(animal.sex))
# print("weight".format(animal.weight))

# print(animal.age)
# print(animal.sex)
# print(animal.weight)

# #6.4
# def get_car():
#     return {"movable" : True,  "passengers" : [], "is_running" : False}
# def load_passenger(car, passenger):
#     car["passengers"].append(passenger)
# def run(car):
#     car["is_running"] = True
# car = get_car()
# load_passenger(car, "old driver")
# run(car)
# print(car)

# class Account:
#     """定义银行账户类"""
#
#     interest_rate = 0.0668  # 类变量利率 ①
#
#     def __init__(self, owner, amount):
#         self.owner = owner  # 定义实例变量账户名
#         self.amount = amount  # 定义实例变量账户金额
#
# account = Account('Tony', 1_800_000.0)
#
# print('账户名：{}'.format(account.owner)) # ② 实例名.实例变量
# print('账户金额：{:,}'.format(account.amount))
# print('利率：{}'.format(Account.interest_rate)) # ③ 类名.类变量
#
#
#todo : .format makes int & str together
#todo : also, {print("{:.2f}".format(3.1415926))}
#todo : --> 3.14
#
#  number   format  output      description
# 3.1415926	{:.2f}	3.14	    保留小数点后两位
# 3.1415926	{:+.2f}	+3.14	    带符号保留小数点后两位         float
# -1	    {:+.2f}	-1.00	    带符号保留小数点后两位
# 2.71828	{:.0f}	3	        不带小数
# 5	        {:0>2d}	05	        数字补零 (填充左边, 宽度为2)   integer
# 5	        {:x<4d}	5xxx	    数字补x (填充右边, 宽度为4)
# 10	    {:x<4d}	10xx	    数字补x (填充右边, 宽度为4)
# 1000000	{:,}	1,000,000	以逗号分隔的数字格式
# 0.25	    {:.2%}	25.00%	    百分比格式
# 10^8  	{:.2e}	1.00e+09	指数记法
# 13	    {:>10d}	    13	    右对齐 (默认, 宽度为10)
# 13	    {:<10d}	    13	    左对齐 (宽度为10)
# 13	    {:^10d}	    13	    中间对齐 (宽度为10)
#

class Account:
    """定义银行账户类"""

    interest_rate = 0.0668  # 类变量利率

    def __init__(self, owner, amount):
        self.owner = owner  # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额

    # 类方法
    @classmethod
    def interest_by(cls, amt): #①
        return cls.interest_rate * amt #②

interest = Account.interest_by(12_000.0) #③
print('计算利息：{0:.4f}'.format(interest))

# 定义类方法有两个关键：
# 一、方法第一个参数cls，见代码①行，cls是类的type实例，type是描述Python数据类型的类；
# 二、方法使用装饰器@classmethod声明该方法是类方法。
#
# 代码第②行是方法体，在类方法中可以访问其他的类变量和类方法, cls.interest_rate是访问类变量interest_rate。
#
# 代码第③行是调用类方法interest_by()，采用“类名.类方法”形式调用。










# import math
#
# class Circle(object):
#     def __init__(self, radius):
#         print("Space : " + str(math.pi * radius ** 2))
#         print("Circumference : " + str(6.28 * radius))
# if __name__ == '__main__':
#     circle = Circle(int(input("Radius:")))
















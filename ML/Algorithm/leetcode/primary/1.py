# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 10:19
# @Author  : taltalasuka
# @File    : 1.py
# @Software: PyCharm

# def calculate(number):
#     count = 0
#     for i in range(number):
#         if number[i] = 1:
#             count += 1
#     return count
#
# if __name__ == '__main__':
#     calculate()

# this is just my program
# bruh so suck

class Solution(object):

    def hammingWeight(self, n):
        """
        :param n:
        :return last result:
        """
        # solution 1 : function recursion
        return bin(n).count("1")
        #solution 2 : for loop count 1

        #solution 3 : from decimal to binary

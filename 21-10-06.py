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
tuple1 = (1, 3, 5, 7, 9)
#slice#
# print(tuple1[0:3])
# print(tuple1[0:5:2])
# print(tuple1[::-1])
# print(tuple1[-3:-1])
#serch 'in'#
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
zergling = {'attack' : 5, 'speed' : 4.13, 'price' : 50}
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
game = "minecraft"
dict = {}
for i in game:
    dict[i] = dict.get(i, 0) + 1
print(dict)
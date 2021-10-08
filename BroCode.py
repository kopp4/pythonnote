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
# phone_number = '123-456-7890'
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
#
# 16. 2D lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizze", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
# food = [drinks, dinner, dessert]
# print(food[0][1])
#
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
#19. set
utensils = {"fork", "spoon", "knife"}
for x in utensils:
    print(x)                # everytime u print the set value is not ordered








# try:
#     print('ur age is : ' + age)
#     if int(age) <= 0:
#         raise Exception("Age must be above 0")
# except Exception as e:
#     print(e)
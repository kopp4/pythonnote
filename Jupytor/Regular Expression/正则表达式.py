#正则表达式
#
#Regular Expression, regex, regexp, RE, re
#
import re

#  \w letter, int, underline == [A-Za-z0-9_]

# 1.基本元字符
# \ 转义符
#  . Anything
# + 1 or more
# * 0 or more
# ? o or 1
# | select
# {} eg : o{2} : food ; o{2,} : foooooooood {n,m} matching n to m
# [] 定义字符类      []是定义匹配的字符范围。比如 [a-zA-Z0-9] 表示相应位置的字符要匹配英文字符和数字。[\s*]表示空格或者*号。  [\d.]+ 是所有数字包括小数
# () 定义分组
# ^ 表示取反或匹配一行的开始
# $ 匹配一行的结束
#
#re.search
#
#p1 = r"\w+@qq\.com". # raw string
#text = "Proust's email is taltalasuka@qq.com'"
#m = re.search(p1, text)
#print(m)


#
# 2. 字符类
#
#
#eg3:      "^"  ：
#import re

#p = r"[^0123456789]" # matching non-integral chars
#print(re.search(p, "1000"))
#print(re.search(p, "asuka"))

#           -=预定义字符类=-
# .	    匹配任意一个字符(除了换行符)
# \\	匹配反斜杠\字符
# \n	匹配换行
# \r	匹配回车
# \f	匹配一个换页符
# \t	匹配一个水平制表符
# \v	匹配一个垂直制表符
# \s	匹配一个空格符，等价于[\t\n\r\f\v]
# \S	匹配一个非空格符，等价于[^\s]
# \d	匹配一个数字字符，等价于[0-9]
# \D	匹配一个非数字字符，等价于[^0-9]
# \w	匹配任何语言的单词字符、数字和下划线等字符
# \W	等价于[^\w]

#       量词
# ?	出现零次或一次
# *	出现零次或多次
# +	出现一次或多次
# {n}	出现零次或n次
# {n,m}	至少出现n次但不超过m次
# {n,}	至少出现n次
#
#           -=贪婪&懒惰=-
## 使用贪婪量词
# m = re.search(r'\d{5,8}', '87654321')  # 出现数字8次 ①
# print(m)
# 匹配字符'87654321'
#
## 使用惰性量词，在量词后面加“?”
# m = re.search(r'\d{5,8}?', '87654321')  # 出现数字5次 ②
# print(m)
# 匹配字符'87654'
#
#
#           -=分组=-
#       字符串放到一对小括号
#
#
# p = r'(121){2}' #①
# m = re.search(p, '121121abcabc')
# print(m)  # 匹配
# print(m.group())  # 返回匹配字符串 #②
# print(m.group(1))  # 获得第一组内容 #③ 组编号从1开始
#
# p = r'(\d{3,4})-(\d{7,8})' #④
# m = re.search(p, '010-87654321')
# print(m)  # 匹配
# print(m.group())  # 返回匹配字符串
# print(m.groups())  # 获得所有组内容 #⑤
#
#       分组的命名
# 通过在组开头添加“?P<分组名>”实现
#
# p = r'(?P<area_code>\d{3,4})-(?P<phone_code>\d{7,8})' #①
# m = re.search(p, '010-87654321')
# print(m)  # 匹配
# print(m.group())  # 返回匹配字符串
# print(m.groups())  # 获得所有组内容
#
# # 通过组编号返回组内容
# print(m.group(1))
# print(m.group(2))
#
# # 通过组名返回组内容
# print(m.group('area_code')) #②
# print(m.group('phone_code')) #③
#
#todo               SUMMARY
#           .group method tend to have the string named, make it a tuple
#
#
#           -=非捕获分组=-
#
#
#
#           -=search()和match()函数=-
#   match : 输入字符串开始处查找
# p = r'\w+@zhijieketang\.com'
#
# text = "Tony's email is tony_guan588@zhijieketang.com." # ①
# m = re.search(p, text)
# print(m)  # 匹配
#
# m = re.match(p, text)
# print(m)  # 不匹配
#
# email = 'tony_guan588@zhijieketang.com' # ②
# m = re.search(p, email)
# print(m)  # 匹配
#
# m = re.match(p, email)
# print(m)  # 匹配
#
# # match对象常用的几个方法：
# print("match对象几个方法")
# print(m.group()) #返回匹配的子字符串
# print(m.start()) #返回匹配的子字符串的开始索引
# print(m.end())   #返回匹配的子字符串的结束索引
# print(m.span())  #返回匹配的子字符串的跨度
#
#           -=findall()和finditer()函数=-
# p = r'[Jj]ava'
# text = 'I like Java and java.'
#
# match_list = re.findall(p, text)
# print(match_list)
#
# match_iter = re.finditer(p, text)
# for m in match_iter:
#     print(m.group(), end = " ")
#

# s = 'img1.jpg,img2.jpg,img3.bmp'

#           -=捕获分组=-

# p = r'\w+\.jpg' # ①
# mlist = re.findall(p, s)
# print(mlist)

# #不能将限定符与定位符一起使用
#       定位符
# ^	    匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配。
# $	    匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配。
# \b	匹配一个单词边界，即字与空格间的位置。
# \B	非单词边界匹配。
#
#
#           -=字符串替换=-
#
p = r'\d+'
text = 'AB12CD34EF'

repace_text = re.sub(p, ' ', text) # ①
print(repace_text)          # AB CD EF

repace_text = re.sub(p, '*', text, count=1) # ②
print(repace_text)          # AB*CD34EF

repace_text = re.sub(p, ' ', text, count=2) # ③
print(repace_text)          # AB CD EF

#
# --------------------------------------------assignment--------------------------------------------
#1.
# 提取颜色
# content = '''
# 苹果是绿色的
# 橙子是橙色的
# 香蕉是黄色的
# 乌鸦是黑色的'''
#
# p = r".色"
# print(re.findall(p, content))
# #2.
# content='''我的微博密码是：1234567，
# QQ密码是：33445566，
# 银行卡密码是：888888，
# Github密码是：999abc999，帮我记住它们'''
#
# print(re.search("QQ密码是：.+", content))
# #3.
content = '''
Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区 2万/月 02-18满员
测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区 2.5万/每月 02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区 1.3万/每月 02-18剩余11人
测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区 1.1万/每月 02-18剩余5人
Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区 2.8万/月 02-18剩余255人
python开发工程师 上海优似腾软件开发有限公司上海-浦东新区 2.5万/每月 02-18满员
python开发工程师 上海优乐美软件开发有限公司上海-浦东新区5万/每月 02-18满员
'''

print(re.findall("\d?\.?\d万\/每?月", content))

t = re.finditer(r"[\d.]+万/.?月", content)
for i in t:
    print(i.group(), end = " ")
# --------------------------------------------assignment--------------------------------------------


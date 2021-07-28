# coding=gbk
# @file:02-re.py
# @data:2021/7/17 18:53
# Editor:clown
import re

# r的意思 防止转义字符
# findall匹配字符串中所有的符号正则的内容
# lst = re.findall(r"\d+", "我的电话号码是：10086,我女朋友打电话:10005 1651")
# print(lst)

# finditer 匹配字符串中的所有内容 返回迭代器
# it = re.finditer(r"\d+", "我的电话号码是：10086,我女朋友打电话:10005 16515")
# print(it)
# for i in it:
#     print(i)  # 地址匹配地址匹配长度
#     print(i.group())  # 直接匹配关键信息

'''

'''
# 返回结果是match对象   匹配第一个符合的东西， 证明有无一个结果
# s = re.search(r"\d+", "我的电话号码是：10086,我女朋友打电话:10005 16515")
# print(s.group())

# match从头开始匹配
# s = re.match(r"\d+", "10086,我女朋友打电话:10005 16515")
# print(s.group())

# 预加载正则表达式
# s = re.compile(r"\d+")
# ret=s.finditer("我的电话号码是：10086,我女朋友打电话:10005 16515")
# print(ret)
# for i in ret:
#     print(i.group())
#
# ret=s.findall("呵呵哒，我就不信你敢不换我一个亿4798789")
# print(ret)
# for i in ret:
#     print(i)


s= """
<div class='jay'><span id='10010'>嘟嘟</span></div>
<div class='lala'><span id='10011'>clown</span></div>
<div class='jj'><span id='10012'>duck</span></div>
<div class='tory'><span id='10013'>fuck</span></div>
<div class='jay'><span id='10014'>胡说八道</span></div>
"""
#re.S 啥意思 .能匹配换行符   #加上括号(?P<写组名>)
obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahah>.*?)</span></div>",re.S)
result=obj.finditer(s)  #因为经过解释器之后再直接finditer findall都可以
print(result)


print("********************")
for i in result:
    print(i.group())
    print(i.group("wahah"))
    print(i.group("id"))
print("********************")
# ret=obj.findall(obj,s)
# print(ret)
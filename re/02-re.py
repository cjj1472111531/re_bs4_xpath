# coding=gbk
# @file:02-re.py
# @data:2021/7/17 18:53
# Editor:clown
import re

# r����˼ ��ֹת���ַ�
# findallƥ���ַ��������еķ������������
# lst = re.findall(r"\d+", "�ҵĵ绰�����ǣ�10086,��Ů���Ѵ�绰:10005 1651")
# print(lst)

# finditer ƥ���ַ����е��������� ���ص�����
# it = re.finditer(r"\d+", "�ҵĵ绰�����ǣ�10086,��Ů���Ѵ�绰:10005 16515")
# print(it)
# for i in it:
#     print(i)  # ��ַƥ���ַƥ�䳤��
#     print(i.group())  # ֱ��ƥ��ؼ���Ϣ

'''

'''
# ���ؽ����match����   ƥ���һ�����ϵĶ����� ֤������һ�����
# s = re.search(r"\d+", "�ҵĵ绰�����ǣ�10086,��Ů���Ѵ�绰:10005 16515")
# print(s.group())

# match��ͷ��ʼƥ��
# s = re.match(r"\d+", "10086,��Ů���Ѵ�绰:10005 16515")
# print(s.group())

# Ԥ����������ʽ
# s = re.compile(r"\d+")
# ret=s.finditer("�ҵĵ绰�����ǣ�10086,��Ů���Ѵ�绰:10005 16515")
# print(ret)
# for i in ret:
#     print(i.group())
#
# ret=s.findall("�Ǻ��գ��ҾͲ�����Ҳ�����һ����4798789")
# print(ret)
# for i in ret:
#     print(i)


s= """
<div class='jay'><span id='10010'>��</span></div>
<div class='lala'><span id='10011'>clown</span></div>
<div class='jj'><span id='10012'>duck</span></div>
<div class='tory'><span id='10013'>fuck</span></div>
<div class='jay'><span id='10014'>��˵�˵�</span></div>
"""
#re.S ɶ��˼ .��ƥ�任�з�   #��������(?P<д����>)
obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahah>.*?)</span></div>",re.S)
result=obj.finditer(s)  #��Ϊ����������֮����ֱ��finditer findall������
print(result)


print("********************")
for i in result:
    print(i.group())
    print(i.group("wahah"))
    print(i.group("id"))
print("********************")
# ret=obj.findall(obj,s)
# print(ret)
# coding=gbk
# @file:04-���е�������.py
# @data:2021/7/22 22:07
# Editor:clown

# 1.��λ��2021�ȿ�Ƭ
# 2.��2021�ؿ�Ƭ����ȡ����ҳ������ӵ�ַ
# 3.��������ҳ������ӵ�ַ���õ�������Ҫ�����ص�ַ
import re

import requests
url="https://www.dy2018.com/"
heads={
"User-Agent": "Mozilla/5.0 (WindowsNT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
#False verify=False ������ ȥ����ȫ��֤
resp=requests.get(url,headers=heads,verify=False)
resp.encoding='gb2312' #�����Ѵ������ ָ���ַ���

obj1=re.compile(r"2021�ؿ���Ƭ.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2=re.compile(r"<li><a href='(?P<wangzhan>.*?)'.*?>(?P<mingzi>.*?)</a>",re.S) #��ȡ������������������
obj3 = re.compile(r'<div class="title_all"><h1>(?P<mingzi>.*?)'
                  r'<div class="position"><span>���֣�<strong class="rank">(?P<score>.*?)'
                  r"'>(?P<leixing>.*?)</a>", re.S)
obj4 = re.compile(r'��Ƭ������(?P<movie>.*?)<br />',re.S)

# print("-"*30)
result=obj1.finditer(resp.text)
child_herflist=[]
for i in result:
    # print(i.group("ul"))
    ul=i.group("ul")
    #��ȡ������ҳ������
    result1=obj2.finditer(ul)
    for iit in result1:
        # ƴ����ҳ���url��ַ����ַ������ҳ���ַ
        child_href=url+iit.group("wangzhan").strip("/")
        child_herflist.append(child_href)
        # print(child_href)
        # print(iit.group("mingzi"))
# print("-"*30)
# for j in child_herflist:  //�������
#     print(j)
# print("-"*30)

# print("-"*30)
#��ȡ��ҳ������ ������ҳ���һ������ ����֮��
for herf in child_herflist:
    print(herf) #��ӡ�б���ÿһ����ַ
    child_resp=requests.get(herf,verify=False)
    child_resp.encoding='gb2312'
    # print(child_resp.text) #�鿴ҳ��Դ��
    rrr=obj4.search(child_resp.text)
    print(rrr.group("movie"))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # break  #���ڲ�������
    # print(s.group("score"),end=" ")
    # print("Ƭ��������"+s.group("leixing"))
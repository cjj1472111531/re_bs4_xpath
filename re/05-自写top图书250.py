# coding=gbk
# @file:05-自写top图书250.py
# @data:2021/7/25 18:54
# Editor:clown
import csv

from bs4 import BeautifulSoup
import requests
import re
requests.packages.urllib3.disable_warnings()

head={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url="https://book.douban.com/top250"
resp=requests.get(url,headers=head)
# resp.encoding='utf-8'
pagecont=resp.text
# print(pagecont)
obj=re.compile(r'<a href="(.*?)&#34; title="(?P<mingzi>.*?)"'
               r'.*?<span class="rating_nums">(?P<pingfen>.*?)</span>'
               r'.*?<span class="inq">(?P<pinglun>.*?)</span>',re.S)
               # r'.*?<span class="p1">(?P<number>.*?)人评论</span>'
               # r'.*?<span class="inq">(?P<pinglun>.*?)</span>',re.S)

result=obj.finditer(pagecont)
# print("-"*30)
# if result:
#     print(result)
# print("-"*30)
f=open("clown.csv",mode="w",encoding="utf-8")
csvss=csv.writer(f)

idc=[] #设置一个列表来装
for i in result:
    if i:
        # print(i.group("mingzi"),end="---")
        # print(i.group("pingfen"),end="---")
        # # print(i.group("number"),end="---")
        # print(i.group("pinglun"))
        idc.append(i.groupdict())
        dic=i.groupdict()

        csvss.writerow(dic.values())
print(idc)
print("over")
f.close()
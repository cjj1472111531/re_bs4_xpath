# coding=gbk
# @file:03-����top250.py
# @data:2021/7/20 21:52
# Editor:clown
import re
import requests
import csv
#��ҳ��Դ���룬request
url="https://movie.douban.com/top250"
head={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
resp=requests.get(url,headers=head)
page_content=resp.text

#��������
#obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
#               r'.*?<span class="other">(?P<bieming>.*?)</span>.*?</li>',re.S)
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
               r'.*?<p class="">.*?<br>(?P<niandai>.*?)&nbsp'
               r'.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>'
               r'.*?<div class="star">.*?<span>(?P<number>.*?)������</span>'
               r'.*?<span class="inq">(?P<pingyu>.*?)</span>',re.S)
# obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>',re.S)
#��ʼƥ��
reult=obj.finditer(page_content)
f=open("data.csv",mode="w")
csvwriter=csv.writer(f)

for i in reult:
    # print(i.group("name"),end="---")
    # print(i.group("niandai").strip(),end="---")
    # print("����Ϊ��"+i.group("pingfen"),end="---")
    # print(i.group("number")+"������",end="---")
    # print("����Ϊ��"+i.group("pingyu"))
    # print(i.group("bieming"))
    dic=i.groupdict()
    dic['niandai']=dic['niandai'].strip()
    # print(dic)
    csvwriter.writerow(dic.values())
# print(resp.text)
print("over")
f.close()

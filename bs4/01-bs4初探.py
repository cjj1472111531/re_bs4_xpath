# coding=gbk
# @file:01-bs4��̽.py
# @data:2021/7/25 13:28
# Editor:clown
from bs4 import BeautifulSoup
import requests
import re
head={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url="https://book.douban.com/top250"
resp=requests.post(url,headers=head)
resp.encoding='utf-8'
# print(resp.text)

#��������
#1.��ҳ��Դ���뽻��BeautifulSoup���д�������bs����
#beautiful
page=BeautifulSoup(resp.text,"html.parser") #ָ��html������
#2.��bs�����в�������
# lala=page.find_all("div",class_="pl2") #class �ǹؼ��� ����û�취��
#lala=page.find_all("div",attrs={"div":"pl2"}) #��΢���鷳��
lala=page.find_all("table")
# print(lala)
# lala=str(lala)

''' re������ '''
obj1=re.compile(r'<span class="inq">(?P<shuming>.*?)</span>',re.S)#������

''' ���������� '''
for i in lala:
    number= i.find_all("span", class_='p1')
    zz=i.find_all("span",class_='inq')#����
    print("-"*30)
    # print(number[0].text,end=" ")#����
    # print(zscore[1].text,end=" ")#����
    print(zz[0].text) #.text ��ʾ�õ�����ǩ��ǵ�����
    print("-"*30)

# little=lala.find("td",valign="top") #һС�ε�top250ͼ��


# for i in lala:
#     little=i.find("td",valign="top") #һС�ε�top250ͼ��
#     shuming1=obj1.finditer(little)
#     # print(shuming1)
#     print("-"*30)







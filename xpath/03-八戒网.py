# coding=gbk
# @file:03-�˽���.py
# @data:2021/7/27 20:01
# Editor:clown
#�õ�ҳ��Դ����
#��ȡ�ͽ�������
from lxml import etree
from bs4 import BeautifulSoup
import requests
import re
url="https://yongzhou.zbj.com/search/f/?type=new&kw=saas"
head={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

#re
res=re.compile(r'<p class="title">(?P<www>.*?)</p>',re.S)
ggg=re.compile(r'<p class="text-overflow">.*?>(?P<company>.*?)</p>',re.S)
ddd=re.compile(r'<span title="<=(?P<diqu>.*?)".*?</span>')


resp=requests.get(url,headers=head)
resp.encoding="utf-8"
resp=resp.text
# print(resp.text)

'''bs4 ����'''
page=BeautifulSoup(resp,"html.parser")
# clown=page.find_all("div",class_="service-info-wrap")#����
clown=page.find_all("div",class_="service-title")#��Ʒ������һͼ
# print(clown)
# clown1=BeautifulSoup(clown[0].text)
fw=[]
for i in clown:
    xin=str(i)
    # print(type(i))
    # print(xifen)
    ccc=BeautifulSoup(xin,"lxml")
    bb=ccc.find('p',class_="title") #������ռ�ı�ǩ
    # print(bb) #ֱ���ñ�ǩ��������
    bb=str(bb)
    zz=res.finditer(bb)
    for i in zz:
        #��˾���б���
        fw.append(i.group("www"))
        # print(i.group("www"))   #��վ�Ϸ�������д����

gs=[]
ghost=page.find_all("div",class_="service-shop clearfix")
for i in ghost:
    i=str(i)
    # print(i)
    f=BeautifulSoup(i,"lxml")
    gongsi=f.find("p",class_="text-overflow")
    # print(gongsi)

    gongsi=str(gongsi)
    lal=ggg.finditer(gongsi)
    for r in lal:
        gs.append(r.group("company").strip())
        # print(r.group("company").strip())

cjj=page.find_all("div",class_="ico city-icon")
# print(cjj)  #��һ�����ݾ���
# print(ghost)

for j in gs:
    print(j)
    print("-"*30)

#zip L�����б����
# for i,j in zip(gs,fw):
#     print(i,"--",j.strip('<i class="tag-img"></i></span>'))
# print(gs)
# print(fw)



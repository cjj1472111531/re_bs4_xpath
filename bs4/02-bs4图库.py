# coding=gbk
# @file:02-bs4ͼ��.py
# @data:2021/7/25 21:22
# Editor:clown
#1.�õ���ҳ��Դ���룬Ȼ����ȡ����ҳ������ӣ�href
#2.ͨ��href�õ���ҳ������ݣ�����ҳ�����ҵ�ͼƬ������ img ->src
#3.����ͼƬ
import requests
import re
from bs4 import BeautifulSoup
url="http://www.netbian.com/"
head={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
resp=requests.get(url,headers=head)
resp.encoding="gbk"
resp=resp.text
# print(resp.text)

#����
clown=BeautifulSoup(resp,"html.parser")
'''
�ӵ�����һ��div����list������Ѱ���е�a��ǩ��ֵ
'''
lala=clown.find("div",class_="list").find_all("a") #�ѷ�Χֱ����С��С��Χ��ͼƬ��ַ
# print(lala)

list=[]
for a in lala:
    # print(a.get("href"))#������������ñ�ǩ��ֵ ֱ��get
    list.append(a.get("href"))

# print(list)

new_list=[]
z=0 #��Ϊ���ĸ����ǶԵ�
for j in list:
    new_url=url+j.strip("/")
    # print(new_url)
    z+=1
    if z>=4:
        new_list.append(new_url)  #�����������վ������
print(new_list)
#��ÿһ��ͼƬ���ص�ַ������
'''
 ͬ������ �ȸ���div class ��������еķ�Χ��С
��С֮��find_all �ҵ����еı�ǩ
֪��֮���������һ��ֵ ��ֵ��֮����get������ȡ��ǩ�о����ֵ����
'''
# for ii in new_list:
#     #����request����������վ
#     child_page_resp=requests.get(ii,headers=head)
#     # �ѱ������͸��� ����ı���ʽ
#     child_page_resp.encoding="gbk"
#     child_page_resp=child_page_resp.text
#     ccc=BeautifulSoup(child_page_resp,"html.parser")
#     ghost=ccc.find()

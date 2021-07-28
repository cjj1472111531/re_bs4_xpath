# coding=gbk
# @file:01-bs4初探.py
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

#解析数据
#1.把页面源代码交给BeautifulSoup进行吹，生成bs对象
#beautiful
page=BeautifulSoup(resp.text,"html.parser") #指定html解析器
#2.从bs对象中查找数据
# lala=page.find_all("div",class_="pl2") #class 是关键字 所以没办法做
#lala=page.find_all("div",attrs={"div":"pl2"}) #稍微更麻烦了
lala=page.find_all("table")
# print(lala)
# lala=str(lala)

''' re正则表达 '''
obj1=re.compile(r'<span class="inq">(?P<shuming>.*?)</span>',re.S)#书名字

''' 靓汤正则表达 '''
for i in lala:
    number= i.find_all("span", class_='p1')
    zz=i.find_all("span",class_='inq')#评语
    print("-"*30)
    # print(number[0].text,end=" ")#作者
    # print(zscore[1].text,end=" ")#评分
    print(zz[0].text) #.text 表示拿到被标签标记的内容
    print("-"*30)

# little=lala.find("td",valign="top") #一小段的top250图书


# for i in lala:
#     little=i.find("td",valign="top") #一小段的top250图书
#     shuming1=obj1.finditer(little)
#     # print(shuming1)
#     print("-"*30)







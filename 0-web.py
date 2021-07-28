# coding=gbk
# @file:0-web.py
# @data:2021/7/13 22:22
# Editor:clown
# 爬虫：通过编写程序来获取奥互联网资源
# 百度   需求：用程序模拟浏览器 从网站获取资源和内容
from bs4 import  BeautifulSoup
import requests
# re=requests.get('http://www.baidu.com')
# print(re.content.decode('utf-8'))
# homepage=re.content.decode() #解码
# soup=BeautifulSoup(homepage,'html.parser')
# script=soup.find(id='lg')
# print(script)
from urllib.request import urlopen  #网址相关的库  url 网址 open打开


url='http://www.baidu.com'
response=urlopen(url)

print("***************")

# print(response.read().decode())

with open("baidu.html", mode='w', encoding='utf-8') as f:
    # z=response.read().decode("utf-8")
    # print(z)
    f.write(response.read().decode("utf-8"))
    f.close()
print("over!")




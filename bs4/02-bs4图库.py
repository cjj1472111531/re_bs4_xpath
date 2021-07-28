# coding=gbk
# @file:02-bs4图库.py
# @data:2021/7/25 21:22
# Editor:clown
#1.拿到主页面源代码，然后提取到子页面的链接，href
#2.通过href拿到子页面的内容，从子页面中找到图片的下载 img ->src
#3.下载图片
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

#靓汤
clown=BeautifulSoup(resp,"html.parser")
'''
从单独的一个div块中list类中找寻所有的a标签的值
'''
lala=clown.find("div",class_="list").find_all("a") #把范围直接缩小变小范围的图片地址
# print(lala)

list=[]
for a in lala:
    # print(a.get("href"))#靓汤里面如何拿标签的值 直接get
    list.append(a.get("href"))

# print(list)

new_list=[]
z=0 #因为第四个才是对的
for j in list:
    new_url=url+j.strip("/")
    # print(new_url)
    z+=1
    if z>=4:
        new_list.append(new_url)  #把主界面的网站搞下来
print(new_list)
#把每一个图片下载地址搞下来
'''
 同样解析 先根据div class 把这个所有的范围缩小
缩小之后find_all 找到所有的标签
知道之后把他赋给一个值 赋值玩之后用get函数获取标签中具体的值即可
'''
# for ii in new_list:
#     #继续request解析数据网站
#     child_page_resp=requests.get(ii,headers=head)
#     # 把编码类型改了 变成文本格式
#     child_page_resp.encoding="gbk"
#     child_page_resp=child_page_resp.text
#     ccc=BeautifulSoup(child_page_resp,"html.parser")
#     ghost=ccc.find()

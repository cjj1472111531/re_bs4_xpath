# coding=gbk
# @file:04-手刃盗版天堂.py
# @data:2021/7/22 22:07
# Editor:clown

# 1.定位到2021比看片
# 2.从2021必看片中提取到子页面的链接地址
# 3.从请求子页面的链接地址中拿到我们想要的下载地址
import re

import requests
url="https://www.dy2018.com/"
heads={
"User-Agent": "Mozilla/5.0 (WindowsNT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
#False verify=False 就行了 去掉安全验证
resp=requests.get(url,headers=heads,verify=False)
resp.encoding='gb2312' #这样已处理可以 指定字符集

obj1=re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2=re.compile(r"<li><a href='(?P<wangzhan>.*?)'.*?>(?P<mingzi>.*?)</a>",re.S) #从取出来的正则中再正则
obj3 = re.compile(r'<div class="title_all"><h1>(?P<mingzi>.*?)'
                  r'<div class="position"><span>评分：<strong class="rank">(?P<score>.*?)'
                  r"'>(?P<leixing>.*?)</a>", re.S)
obj4 = re.compile(r'◎片　　名(?P<movie>.*?)<br />',re.S)

# print("-"*30)
result=obj1.finditer(resp.text)
child_herflist=[]
for i in result:
    # print(i.group("ul"))
    ul=i.group("ul")
    #提取子链中页面链接
    result1=obj2.finditer(ul)
    for iit in result1:
        # 拼接子页面的url地址：地址加上子页面地址
        child_href=url+iit.group("wangzhan").strip("/")
        child_herflist.append(child_href)
        # print(child_href)
        # print(iit.group("mingzi"))
# print("-"*30)
# for j in child_herflist:  //检测链接
#     print(j)
# print("-"*30)

# print("-"*30)
#提取子页面内容 先是子页面的一个内容 内容之后
for herf in child_herflist:
    print(herf) #打印列表中每一个地址
    child_resp=requests.get(herf,verify=False)
    child_resp.encoding='gb2312'
    # print(child_resp.text) #查看页面源码
    rrr=obj4.search(child_resp.text)
    print(rrr.group("movie"))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # break  #用于测试作用
    # print(s.group("score"),end=" ")
    # print("片名类型是"+s.group("leixing"))
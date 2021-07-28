# coding=gbk
# @file:01-requests_入门.py
# @data:2021/7/13 22:15
# Editor:clown
#安装request
#pip install requests
#国内
#pip install 清华的网址
import requests
query=input("输入一个喜欢的明星")
url=f"http://www.baidu.com/s?wd={query}"
headers={"User-Agent":"Mozilla/5.0 (Wi"
        "ndows NT 10.0; Win64; x64) Ap"
        "pleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.114 Safari/537.36"}
req=requests.get(url,headers=headers) #模仿浏览器 去访问网站
print(req.content.decode())


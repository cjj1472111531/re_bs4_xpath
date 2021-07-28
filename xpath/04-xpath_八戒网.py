# coding=gbk
# @file:04-xpath_八戒网.py
# @data:2021/7/27 22:24
# Editor:clown
from bs4 import BeautifulSoup
from lxml import etree
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
# print(resp)

#是网页源码的话
html=etree.HTML(resp)
#拿到每一个服务商的div 所有得div

divs=html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
# print(divs)
for div in divs:
    '''价格 成交量 备注 地区'''
    #chengjiaoliu=div.xpath('./div/div/a/div/div/span/text()')
    jiazhi=div.xpath('./div/div/a/div[2]/div[1]/span[1]/text()')
    chengjiaoliu=div.xpath('./div/div/a/div[2]/div[1]/span[2]/text()')
    # zz=div.xpath('./*[@id="utopia_widget_74"]/a[1]/div[2]/div[1]/text()')
    print(jiazhi,end="---")
    print(chengjiaoliu,end="---")
    fw=div.xpath('./div/div/a/div[2]/div[2]/p/text()')
    print(fw,end="---")
    gs=div.xpath('./div/div/a[2]/div[1]/p[1]/text()')
    print(gs)
#解析


print("over")


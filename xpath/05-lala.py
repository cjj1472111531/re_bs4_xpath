# coding=gbk
# @file:05-lala.py
# @data:2021/7/28 21:00
# Editor:clown
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
    '''价格 成交量 服务 公司 备注 地区'''
    #chengjiaoliu=div.xpath('./div/div/a/div/div/span/text()')
    '''处理第一个价值 把前面的人民币字符去掉'''
    jiazhi=div.xpath('./div/div/a/div[2]/div[1]/span[1]/text()')
    # print(jiazhi)
    if jiazhi:
        jiazhi_value=jiazhi[0].strip('?')
    else:
        jiazhi_value=0
    # print(jiazhi_value)
    # jiazhi_value=jiazhi[0].strip('?')
    '''处理交易量'''
    chengjiaoliu=div.xpath('./div/div/a/div[2]/div[1]/span[2]/text()')
    if chengjiaoliu:
        cjl_value=chengjiaoliu[0].strip("近半年成交：")
        cjl_value=cjl_value.strip("笔")
    else:
        cjl_value=0
    # print(cjl_value)
    # zz=div.xpath('./*[@id="utopia_widget_74"]/a[1]/div[2]/div[1]/text()')
    # print(jiazhi,end="---")
    '''处理服务'''
    # print(chengjiaoliu)
    fw=div.xpath('./div/div/a[1]/div[2]/div[2]/p/text()')
    if fw:
        fw_value="saas".join(fw)
    else:
        fw_value="空"
    # print(fw_value)
    # print(fw,end="---")
    '''处理公司'''
    gs=div.xpath('./div/div/a[2]/div[1]/p[1]/text()')
    if gs:
        gs_value=gs[1].strip("\n\n")
    else:
        gs_value="空"
    # print(gs_value)
    '''处理地区'''
    diqu=div.xpath('./div/div/a[2]/div[1]/div[1]/span/text()')
    if diqu:
        diqu_value=diqu[0]
    else:
        diqu_value="无"
    # print(diqu_value)
    '''输出 钱 交易量 服务 公司 地区'''
    print(jiazhi_value,"--",cjl_value,"--",fw_value,"--",gs_value,"--"
          ,diqu_value)
#解析


print("over")
# coding=gbk
# @file:text.py
# @data:2021/7/25 12:51
# Editor:clown
import re
import requests
import urllib3
urllib3.disable_warnings()
list=['https://www.dy2018.com/i/103808.html', 'https://www.dy2018.com/i/103562.html', 'https://www.dy2018.com/i/103778.html', 'https://www.dy2018.com/i/103772.html', 'https://www.dy2018.com/i/103751.html', 'https://www.dy2018.com/i/103223.html', 'https://www.dy2018.com/i/103741.html', 'https://www.dy2018.com/i/103726.html', 'https://www.dy2018.com/i/103712.html', 'https://www.dy2018.com/i/103566.html', 'https://www.dy2018.com/i/103690.html', 'https://www.dy2018.com/i/103685.html', 'https://www.dy2018.com/i/101311.html', 'https://www.dy2018.com/i/103610.html', 'https://www.dy2018.com/i/103582.html']
obj4 = re.compile(r"◎片　　名(?P<pianming>.*?)<br />", re.S)
for i in list:
    child_resp = requests.get(i, verify=False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text) #查看页面源码
    result5 = obj4.search(child_resp.text)
    if result5.group("pianming"):
        print(result5.group("pianming"))
    # print(result5.group("score"),end=" ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


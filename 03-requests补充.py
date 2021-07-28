# coding=gbk
# @file:03-requests补充.py
# @data:2021/7/15 21:04
# Editor:clown
import requests
url="https://movie.douban.com/j/chart/top_list"
# 重新封装参数
param={
"type": "24",
"interval_id": "100:90",
"action":"",
"start": 20,
"limit":20,
}
heads={
"User-Agent": "Mozilla/5.0 (WindowsNT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
resp=requests.get(url=url,headers=heads,params=param)
# print(resp.request.headers)
for z in resp.json():
    print(z['title'])

resp.close()

# z=resp.json()[1]['title']
# print(z)
# print(resp.json())
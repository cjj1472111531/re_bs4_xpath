# coding=gbk
# @file:01-requests_����.py
# @data:2021/7/13 22:15
# Editor:clown
#��װrequest
#pip install requests
#����
#pip install �廪����ַ
import requests
query=input("����һ��ϲ��������")
url=f"http://www.baidu.com/s?wd={query}"
headers={"User-Agent":"Mozilla/5.0 (Wi"
        "ndows NT 10.0; Win64; x64) Ap"
        "pleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.114 Safari/537.36"}
req=requests.get(url,headers=headers) #ģ������� ȥ������վ
print(req.content.decode())


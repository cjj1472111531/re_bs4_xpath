# coding=gbk
# @file:0-web.py
# @data:2021/7/13 22:22
# Editor:clown
# ���棺ͨ����д��������ȡ�»�������Դ
# �ٶ�   �����ó���ģ������� ����վ��ȡ��Դ������
from bs4 import  BeautifulSoup
import requests
# re=requests.get('http://www.baidu.com')
# print(re.content.decode('utf-8'))
# homepage=re.content.decode() #����
# soup=BeautifulSoup(homepage,'html.parser')
# script=soup.find(id='lg')
# print(script)
from urllib.request import urlopen  #��ַ��صĿ�  url ��ַ open��


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




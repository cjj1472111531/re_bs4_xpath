# coding=gbk
# @file:02-xpath.py
# @data:2021/7/26 22:01
# Editor:clown
from lxml import etree
''' �����Ǹ�xml�� ֱ��xml   �������վ�Ļ�ֱ����parse'''
tree=etree.parse("b.html")  #���������ҳ
# result=tree.xpath("/html")
# print(result)
result1=tree.xpath("/html/body/ul/li/a")
print(result1)
# result1=tree.xpath("/html/body/ul/li/a/text()")
# print(result1)
'''
#��xpathȡ�����Ļ����������б������д洢  xpath��һ��ʼ���� []Ϊ����
 '''
result1=tree.xpath("/html/body/ul/li[3]/a/text()")#[1]�������ĵ�һ�����ϵ���
print(result1)
result=tree.xpath("/html//a/text()")
print(result)
'''
�����ڱ�ǩ����  
@+��ǩ="��ǩ����ֵ" ==@href='dapao' 
Ѱ��li��a��ǩhref������Ϊ���ڵ�ֵ��ɶ��text����
'''
# result2=tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")
# print(result2)

''' 
��b.html ol��һ������
'''
ol_li_list=tree.xpath("/html/body/ol/li")
for i in ol_li_list:
#   print(i)#�鿴�洢�������ַ
    #��ÿһ��li����ȡ������Ϣ
    clown=i.xpath("./a/text()") #��li�м���Ѱ�ң����Ѱ��
    print(clown[0],end="---")
    # clown1 = i.xpath("./a[@href='dapao']/text()")  # ��li�м���Ѱ�ң����Ѱ��
    # print(clown1)
    # print("-"*30)
    #��֪����ǩ����ɶ����ֵ @��ǩ������
    clown2=i.xpath("./a/@href")
    print(clown2)

'''
�õ�����ֵ ��@����
'''
body_div_list=tree.xpath("/html/body")
for h in body_div_list:
    clown3=h.xpath("./div/@class")
    print(clown3,end="---")
    clown4=h.xpath("./div/text()")
    print(clown4)
    # for z in clown3:
    #     print(z)
    # print(clown3,end=" ")

print("last but lost")

print(tree.xpath("/html/body//li/a/@href"))
#���ݼ���text()   ���ֻ��������ֵ�Ļ� ������  @+����
print(tree.xpath("/html/body/ol/li/a/text()"))
print(tree.xpath('/html/body/div[1]/@class'),end=" ")
print(tree.xpath('/html/body/div[1]/text()'))
# coding=gbk
# @file:02-xpath.py
# @data:2021/7/26 22:01
# Editor:clown
from lxml import etree
''' 假如是个xml中 直接xml   如果是网站的话直接用parse'''
tree=etree.parse("b.html")  #解析这个网页
# result=tree.xpath("/html")
# print(result)
result1=tree.xpath("/html/body/ul/li/a")
print(result1)
# result1=tree.xpath("/html/body/ul/li/a/text()")
# print(result1)
'''
#在xpath取出来的基本上是用列表来进行存储  xpath从一开始数的 []为索引
 '''
result1=tree.xpath("/html/body/ul/li[3]/a/text()")#[1]搜索到的第一个符合的字
print(result1)
result=tree.xpath("/html//a/text()")
print(result)
'''
可以在标签中用  
@+标签="标签属性值" ==@href='dapao' 
寻找li中a标签href中属性为大炮的值是啥的text内容
'''
# result2=tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")
# print(result2)

''' 
在b.html ol做一个遍历
'''
ol_li_list=tree.xpath("/html/body/ol/li")
for i in ol_li_list:
#   print(i)#查看存储的物理地址
    #从每一个li中提取文字信息
    clown=i.xpath("./a/text()") #在li中继续寻找，相对寻找
    print(clown[0],end="---")
    # clown1 = i.xpath("./a[@href='dapao']/text()")  # 在li中继续寻找，相对寻找
    # print(clown1)
    # print("-"*30)
    #想知道标签中有啥其他值 @标签名即可
    clown2=i.xpath("./a/@href")
    print(clown2)

'''
拿到属性值 ：@属性
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
#内容加上text()   如何只是拿属性值的话 就是用  @+属性
print(tree.xpath("/html/body/ol/li/a/text()"))
print(tree.xpath('/html/body/div[1]/@class'),end=" ")
print(tree.xpath('/html/body/div[1]/text()'))
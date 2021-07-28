# coding=gbk
# @file:01-xpath初探.py
# @data:2021/7/26 20:59
# Editor:clown
# xpath 是xml文档中搜索内容的一门语言
# html是xml的一个子集

# book 节点 继承关系  谁包着谁 谁就是谁的父节点

"""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
</book>
"""
# 安装lxml模块
from lxml import etree # 引入etree
xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热热1</nick>
        </div>
        <span>
            <nick>热热热热热2</nick>
        </span>
        <lalala>
            <nick>热热热热热3</nick>
            <z>
                <nick>热热热热热3</nick>
            </z>
        </lalala>
    </author>

    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
# 安装lxml模块
from lxml import etree # 引入etree
'''etree是加载一个文件'''
tree=etree.XML(xml)
# result=tree.xpath("/book") #/表示层级关系，第一个/是根节点
# result=tree.xpath("/book/name/text()")#text()拿文本
# result1=tree.xpath("/book/nick/text()")
#单独一个找一个标签的话 会把同一层节点的同一个标签的所有相符的都弄个出来
#result3=tree.xpath("/book/author/div/nick/text()") #单独一个找一个标签的话
# print(result)
# print(result1)
# print(result3)

'''
   //的意思就是将author父节点中所有的关于nick子节点全部输出
   后代符合这个标签的都拿出来
 '''
# result=tree.xpath("/book/author//nick/text()")
# print(result)
'''
 * 任意节点通配符（会儿） 画一个就是一个节点的意思
'''
# result=tree.xpath("/book/author/*/nick/text()")#后代
# print(result)

result=tree.xpath("/book//nick/text()")
print(result)



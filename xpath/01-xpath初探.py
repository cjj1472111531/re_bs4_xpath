# coding=gbk
# @file:01-xpath��̽.py
# @data:2021/7/26 20:59
# Editor:clown
# xpath ��xml�ĵ����������ݵ�һ������
# html��xml��һ���Ӽ�

# book �ڵ� �̳й�ϵ  ˭����˭ ˭����˭�ĸ��ڵ�

"""
<book>
    <id>1</id>
    <name>Ұ�������</name>
    <price>1.23</price>
    <author>
        <nick>�ܴ�ǿ</nick>
        <nick>������</nick>
    </author>
</book>
"""
# ��װlxmlģ��
from lxml import etree # ����etree
xml = """
<book>
    <id>1</id>
    <name>Ұ�������</name>
    <price>1.23</price>
    <nick>������</nick>
    <author>
        <nick id="10086">�ܴ�ǿ</nick>
        <nick id="10010">������</nick>
        <nick class="joy">�ܽ���</nick>
        <nick class="jolin">������</nick>
        <div>
            <nick>����������1</nick>
        </div>
        <span>
            <nick>����������2</nick>
        </span>
        <lalala>
            <nick>����������3</nick>
            <z>
                <nick>����������3</nick>
            </z>
        </lalala>
    </author>

    <partner>
        <nick id="ppc">���ֳ�</nick>
        <nick id="ppbc">���ֲ���</nick>
    </partner>
</book>
"""
# ��װlxmlģ��
from lxml import etree # ����etree
'''etree�Ǽ���һ���ļ�'''
tree=etree.XML(xml)
# result=tree.xpath("/book") #/��ʾ�㼶��ϵ����һ��/�Ǹ��ڵ�
# result=tree.xpath("/book/name/text()")#text()���ı�
# result1=tree.xpath("/book/nick/text()")
#����һ����һ����ǩ�Ļ� ���ͬһ��ڵ��ͬһ����ǩ����������Ķ�Ū������
#result3=tree.xpath("/book/author/div/nick/text()") #����һ����һ����ǩ�Ļ�
# print(result)
# print(result1)
# print(result3)

'''
   //����˼���ǽ�author���ڵ������еĹ���nick�ӽڵ�ȫ�����
   ������������ǩ�Ķ��ó���
 '''
# result=tree.xpath("/book/author//nick/text()")
# print(result)
'''
 * ����ڵ�ͨ���������� ��һ������һ���ڵ����˼
'''
# result=tree.xpath("/book/author/*/nick/text()")#���
# print(result)

result=tree.xpath("/book//nick/text()")
print(result)




'''
re模块方法
    match
    search
    findall
    sub 替换  可以传入函数  看下面的例子
    split

贪婪与非贪婪
python 数量词默认是贪婪的，总是尝试匹配尽可能多的字符，非贪婪则相反

爬虫
import requests
path = '内容路径'
result = re.match(正则表达式，path)  #去除要的内容
response = requests.get(path)
with open(保存路径,'wb') as wstream:
    wstream.write(response.content)


'''

import re
from errno import EMSGSIZE

phone = '010-12345678'

result = re.match('(\d{3}|\d{4})-(\d{8})$',phone)

# ()表示分组
print(result)
print(result.group())
print(result.groups()) #配合括号取出所有信息 按元组的方式
print(type(result.groups()))
print(result.group(1)) #配合括号取出第一组的信息
print(type(result.group(1)))
print(result.group(2)) #配合括号取出第二组的信息

print('--------分割线1-----------')

#爬虫
msg = '<html><h1>abc</h1></html>'
msg1 = '<html><h1>abc</h1></html>'

result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>',msg)
print(result)
print(result.group(1))
print('--------分割线2-----------')
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>',msg1)   #\1表示引用第一个分组的
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))
print('--------分割线3-----------')
#起名的方式
result = re.match(r'<(?P<name1>[0-9a-zA-Z]+)><(?P<name2>[0-9a-zA-Z]+)>(.+)</(?P=name2)></(?P=name1)>',msg1)   #给分组命名
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))
print('--------分割线4-----------')
a = '张三:12,李四:21'
result = re.sub(r'\d+','1000',a)   #rel 需要是字符串格式
print(a)     #并不会修改原始的a
print(result)

#也可以传入函数
def func(temp):
    num = temp.group()
    num1 = int(num)+1
    return str(num1)

result = re.sub(r'\d+',func,a)   #rel 需要是字符串格式
print(result)

print('------split---------')

result = re.split(r'[,:]',a)  #切割后以元组的形式返回
print(result)

print('-----贪婪非贪婪-------')
msg = 'abc123abc'
result1 = re.match(r'abc(\d+)',msg)  #贪婪
result2 = re.match(r'abc(\d+?)',msg) #非贪婪
print(result1)
print(result2)



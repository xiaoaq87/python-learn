'''
正则表达式是对字符串操作的一种逻辑公式
re模块

\A 表示从字符串的开始处匹配
\Z 表示从字符串的结束处匹配，如果存在换行，只匹配到换行前的结束字符串
\b 匹配一个单词边界，也就是指单词和空格间的位置。例如
\B 匹配一个非单词边界           border
\d 匹配任意数字 等价于[0-9]    digit
\D 匹配任意非数字字符 等价于[^\d]
\s 匹配任意空白字符 等价于[\t\n\r\f]   space
\S 匹配任意非空白字符 等价于[^\s]
\w 匹配任意字母数字及下划线 等价于[a-zA-Z0-9_]    word
\W 匹配任意非字母数字及下划线 等价于[^\w]
\\ 匹配原意的反斜杠\


.  用于匹配除换行符（\n）之外的所有字符
^  用于匹配字符串的开始，即行首
$  用于匹配字符串的末尾（末尾如果是\n，就匹配\n的字符）

次数类的
* 用于将前面的模式匹配0次或多次（贪婪模式 即尽可能的多匹配）
+ 用于将前面的模式匹配1次或多次（贪婪模式）
？ 用于将来前面的模式匹配0次或1次（贪婪模式）
*？  +？  ？？ 即上面三种特殊字符的非贪婪模式（尽可能少匹配）
{m} 用于将前面的模式匹配m次
{m,} 用于将前面的模式匹配m次及以上 >=m
{m,n} 用于将前面的模式匹配m次到n次（贪婪模式），即最小匹配m次，最大匹配n次  >=m  <=n
{m,n}？ 即上面的非贪婪模式
\ 转义字符，比如\+ 代表加号的含义
| 比如A|B用于匹配A或B

[] :标识一组字符，占据一个字符位如果^是第一个字符，则表示的是一个补集 [0-9]  [0-9a-zA-Z] [12345]  [a-z]  [^0-9] --数字以外的
( ) 分组

分组  |
注意区别(word1|word2|word3)  [abc],前者表示或者word1或者word2或者word3

'''
import re

msg = '佟丽娅娜扎热巴代斯佟丽娅'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)  #从头开始匹配，如果开头没有则返回None
print(result)

#使用正则re模块方法：match
s = '娜扎佟丽娅热巴代斯'
result = re.match('佟丽娅',s) #从开头匹配，匹配没成功就返回None
print(result)

result = re.search('佟丽娅',s)#search字符串匹配，不限于开头,匹配到第一个就不继续匹配了
print(result)
print(result.span()) #获取匹配的位置
print(result.group()) #使用group提取匹配的内容
print(result.groups())

print('-----------分界线----------')
#a2b  h6k
msg = 'abcd7vjkfd8hdf00'
result = re.search('[a-z][0-9][a-z]',msg)
print(result)
print(result.group())

result = re.findall('[a-z][0-9][a-z]',msg)  #把所有匹配的都找出来
print(result)    #用列表形式返回所有匹配到的

#a7a a88a a7878a
msg = 'a7a0pa88akjgka7878a'
result = re.findall('[a-z][0-9]+[a-z]',msg)
print(result)

#用户名可以是字母数字，不能是数字开头，用户名长度必须6位以上
usename = 'sdf321'
result = re.match('^[^0-9][0-9a-zA-Z]{5,}$',usename)
print(result.group())

msg = 'aa.py ab.txt bb.py kk.png uu.py apyb.xtxt'
result = re.findall(r'\w+\.py\b',msg) #有正则符号有\ 最好前面都加r‘’
print(result)

#匹配0-100数字
n = '100'
result = re.match(r'[1-9]?\d?$|100$',n)
print(result.group())
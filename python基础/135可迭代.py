'''
可迭代的对象：
1、生成器
2、集合、列表、元组、字典、字符串
如何判断一个对象是否可迭代
isinstance()
迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历对象位置的对象
迭代器对对象从集合的第一个元素开始访问，知道所有元素被访问结束
迭代器只能往前不会退后
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

可迭代的 是不是肯定就是 迭代器
生成器是可迭代，也是迭代器，是否是迭代器看是不是可以使用next()
元组、集合、字典、列表不是迭代器，iter(列表)就可以转换为迭代器

生成器是迭代器的一种，

'''
from collections import Iterable

list1 = [1,4,7,8,8]
f = isinstance(list1,Iterable)
print(f)

g1 = iter(list1)  #通过iter函数将列表转换为迭代器

g2 = (x+1 for x in range(10))
f2 = isinstance(g2,Iterable)
print(f2)
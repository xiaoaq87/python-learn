'''
1、如果内部定义的方法 名字相同，后面的那个会覆盖前面那个
2、python允许多继承
class 子类（父类1，父类2[，父类3]）
搜索顺序：子类 类1 类2  类3  object

方法一
print(子类.__mro__)

方法二
import inspect
print(inspect.getmro(子类))  返回元组，反映其搜索顺序，作用和上面一样


经典类 新式类搜索顺序在python2不同,但在python 3相同



'''
import inspect

class Person:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('-----eat1')
    def eat(self,food):
        print('-----eat1,food')

print('------分隔符-----')


#经典类  顺序：从左至右  深度优先
class P1:
    def foo(self):
        print('p1-foo')

class P2:
    def foo(self):
        print('p2-foo')

    def bar(self):
        print('p2-bar')

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print('c2-bar')

class D(C1,C2):
    pass

d = D()
d.foo()
d.bar()
print(D.__mro__)

#新式类    广度优先
# class P1(object):
#     def foo(self):
#         print('p1-foo')
#
# class P2(object):
#     def foo(self):
#         print('p2-foo')
#
#     def bar(self):
#         print('p2-bar')
#
# class C1(P1,P2):
#     pass
#
# class C2(P1,P2):
#     def bar(self):
#         print('c2-bar')
#
# class D(C1,C2):
#     pass
#
# d = D()
# d.foo()
# d.bar()
# print(D.__mro__)
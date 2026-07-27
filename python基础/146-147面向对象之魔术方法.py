'''
__init__:初始化魔术方法
触发时机：初始化对象时候触发（不是实例化触发，但和实例化在一个操作）
__new__：实例化的魔术方法
触发时机：在实例化时触发
实例化就是创建对象的时候

__call__:对象调用方法
触发时机：把对象当函数使用时
调用 对象()
—
__del__:析构魔术方法
触发时机：当对象没有用（没有任何变量引用）的时候被触发

1、对象赋值
p = Person1
p1 = p
说明：p p1指向共同的ige地址，常量赋值也是类似特定
2、删除地址引用
del p1 删除p1对地址的引用
3、查看地址引用个数
import sys
print(sys.getrefcount(p))  这个函数本身也引用了一次
4、没有任何引用时，默认执行__del__的代码
当所有代码都执行完毕时，python解释器会回收所有开辟的内存空间，这时候没有任何引用会触发执行__del__的代码


'''

import sys
class Person:
    def __init__(self):
        print('-----init',self)
        # self.name = name
    def __new__(cls, *args, **kwargs):
        print('-----new')
        position =  object.__new__(cls, *args, **kwargs)
        print(position)
        return position
    def __call__(self, *args, **kwargs):
        print('-------call')

p = Person()
print(p)      #地址与position一样,也与__init__中的self一样

p()  #把对象当函数使用时

'''
1、__new__表示新开辟空间，当创建对象时，先进入__new__申请新开辟内存空间
object.__new__(cls, *args, **kwargs)表示申请开辟一个内存空间，通过return返回出来
object.__new__(cls, *args, **kwargs)就是一个内存地址
2、__init__执行前要先传入一个内存地址，传入的就是return返回出来的内存地址，如果没有return返回出
内存地址，就没办法执行__init__
3、__init__执行完成后，将内存地址赋值给P，创建对象



'''

class Person1:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print('----del---')

p = Person1('jack')
p1 = p #p1 p2 p都指向相同内存地址
p2 = p
p2.name = 'TOM'
print(p.name)

del p2  #删除p2对该地址的引用

print(p.name)
#print(p2.name)  #p2地址引用被删除，这样调用就会报错


print(sys.getrefcount(p))  #查看有多少个p对应的地址被引用，调这个函数的时候也用了一次

#1、集合推导式  格式{}

list1 = [1,2,1,3,5,2,1]
set1 = {x for x in list1}  #集合不能有重复得，自动去除重复项
set2 = {x for x in list1 if x>2}
print(set1)
print(set2)


#2、字典推导式
dict1 = {'a':'A','b':'B','c':'C','d':'C'}

newdict1 = {value:key for key,value in dict1.items()}
print(newdict1)

'''
3、生成器:generator
列表生成式（推导式）可以创建列表，但会占据存储空间，如果列表元素能够按某种算法推算出来，那就不必创建完整得列表
在PYTHON中一边循环一边计算得机制，成为生成器
3.1得到生成器的方式
（1）通过列表推导式得到生成器，圆括号
方式一：通过调用__next__()得到元素
方式二：next(生成器)
每调用一次会产生一个元素，没有调用就不会产生，但超过范围的话会报错（StopIteration）
(2)借助函数完成
函数出现yield关键字，就不是函数，是生成器
步骤
1、定义一个函数，函数中要使用yield关键字
2、调用函数，接收调用的结果
3、得到的结果是生成器
4、借助于next()、_next_得到元素

'''
#（1）通过列表推导式得到生成器，圆括号
g = (x*3 for x in range(20)) #是圆括号
print(type(g))  #generator类
print(g.__next__())  #每次调用才会产生一个,调用必须print
print(next(g))

while True:
    try:
        e = next(g)
        print(e)
    except:
        print('没有更多元素')
        break
#(2)借助函数完成
def func():
    n = 0
    while True:
        n+=1
        yield n  #等效  return + 暂停

g2 = func()
print(type(g2))  #generator类

print(next(g2))
print(next(g2))

#斐波那契数列
def fib(length):
    a,b = 0,1
    n = 2
    while n < length-2:
        a,b = b,a+b
        n+=1
        yield b
    return '没有更多元素' #超过范围可以通过return发出提示信息
g3 = fib(8)
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3)) #超过范围可以通过return发出提示信息

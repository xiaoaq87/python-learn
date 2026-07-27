'''
1、生成器方法：
_next_():获取下一个数据
send(value):向每次生成器调用中传值，第一次调用send(None)

用途：在协程里面会使用
一个进程包含多个线程，一个线程包含多个协程
进程 > 线程 > 协程
交替完成任务


'''


def gen():
    i = 0
    while i < 5:
        temp = yield i     #yield暂停的下一步会把send传输的信息赋值给temp,但一开始没进入循环所有send一开始传递的信息必须是None
        print('temp:',temp)
        i+=1
    return '没有更多数据'

g = gen()

print(g.send(None))   #一开始要None 还没进入循环，没法直接赋值给temp
print(g.send('呵呵'))
print(g.send('哦哦'))


def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield None

def task2(n):
    for i in range(n):
        print('正在听第{}首歌'.format(i))
        yield None
g1 = task1(5)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break



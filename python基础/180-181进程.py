'''
单核：多任务交替执行
多核：可以不同核心执行不同任务，但任务还是会多于核心

并发和并行
并发（concurrent）：多个线程在操作时，如果只有一个CPU，不可能同时执行多个线程，将运行时间切分成若干段，分给不同的进程，一个进程执行时，其他进程挂起
并行（parallel）:当系统有多个CPU，则可以一个CPU执行一个进程，另一个CPU执行另一个进程，两个进程互不干扰
实现多任务的方式
 多进程模式
 多线程模式
 协程
    进城》线程》协程

CTRl + 点击鼠标左键  可以进入内部代码

Process(target= 函数,name = 进程的名字 ,args = (元组)) 这是一个进程对象
对象调用方法：
Process.start()  启动进程并执行任务
Process.run()   只是执行任务 但没有启动进程
terminate() 终止

多进程对全局变量的访问，在每个全局变量里面都放一个全局变量,保证每个进程访问变量都互不干扰，不管这个全局变量是可变变量还是不可变变量
常量 元组  等是不可变变量，列表等是可变变量


'''
import os
# 进程创建
from multiprocessing import Process
from time import sleep

m = 1
def task1(s):
    global m
    while True:
        sleep(s)
        m+=1
        print(m,'这是任务1.......',os.getpid(),'---',os.getppid()) #getpid获得进程编号 getppid获得父进程编号


def task2(s):
    global m
    while True:
        sleep(s)
        m+=1
        print(m,'这是任务2.......',os.getpid(),'----',os.getppid())

#python 开启了一个主进程，然后又开启了下面的两个子进程

number = 1
if __name__ == '__main__':
    p1 = Process(target=task1, name='任务1',args=(1,))   #args参数传入必须是元组
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name='任务2',args=(2,))
    p2.start()
    print(p2.name)

    while True:
        number +=1
        sleep(0.1)
        if number == 100:
            p1.terminate()
            p2.terminate()
            break
        else:
            print(number)

    print('------------')

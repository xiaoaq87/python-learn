'''
当需要创建的进程数量不多的时候，可以直接利用multiprocessing中的Process动态创建多个进程；
但如果需要创建的数量成百上千的时候，可以利用multiprocessing模块中提供的方法Pool方法
初始化Pool可以指定一个最大进程数，但如果池中的进程数已经达到指定的最大值，那么请求就会等待
直到池中有进程结束，才会创建新的进程


非阻塞式进程：全部添加到队列中，立刻返回，并没有等待其他进程执行完毕，但是回调函数，等待任务完成后才调用
阻塞式进程：


'''
import os
import time
from multiprocessing import Pool
from multiprocessing import Process
from random import random

#
# class MyProcess(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     #重写run()
#     def run(self):
#         n = 1
#         while True:
#             print('{}--------自定义进程,n:{}'.format(n,self.name))
#             n+=1
#
# if __name__ == '__main__':
#     p1 = MyProcess('小红')
#     p1.start()
#     p2 = MyProcess('小蓝')
#     p2.start()

print('----分割线1------，进程号：',os.getpid())  #会打印6次，是因为主进程+5个子进程加载导致的

def task(task_name):
    print('开始做任务了！',task_name)
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    # print('完成任务！用时：',(end-start))
    return '完成任务！用时{},进程号{},主进程号{}'.format(end-start,os.getpid(),os.getppid())

container = []

def callback_func(n):    #回调方法必须传入参数
    container.append(n)

print('----分割线2------，进程号：',os.getpid())  #会打印6次，是因为主进程+5个子进程加载导致的
if __name__ == '__main__':
    pool = Pool(5)


    tasks = ['起床','刷牙','叠被子','做饭','吃饭','洗碗','听音乐','拖地板']
    for task1 in tasks:
        pool.apply_async(task,args=(task1,),callback=callback_func)   #添加非阻塞式进程  async 异步
                                                                    #callback可选项，相当于将task函数return值传入callback函数

    print('----分割线3------，进程号：', os.getpid())  # 会打印1次，主进程加载导致的
    pool.close()    #添加任务结束
    pool.join()     #子进程没结束卡住，不让主进程继续往下，在pool 如果主进程结束，子进程就结束了
    print(container)   #与Process对全局变量处理不太同，Process 会给每个进程分配该全局变量，互相不影响，而Pool 则不太一样
    print('任务结束！')



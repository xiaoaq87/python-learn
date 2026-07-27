'''
阻塞式：添加一个执行一个，如果一个任务未结束，下一个就不能进行

进程池
pool =Pool(max)  创造进程对象
pool.apply   阻塞
pool.apply_async()  非阻塞

pool.close()
pool.join()   卡住不让主进程结束

进程间的通信
可以在进程间搭建一个通道--队列 来实现进程间的通信
q = Queue(max)
q = put(self,obj[,block=True,timeout=None]) block表示是否堵塞 timeout=None表示无限，当timeout 有对应值，如果超过该时间还没空间会报异常
q.full()  判断队列是否满了  返回布尔值
q.empty() 判断队列是否空了了  返回布尔值
q.qsize()   判断队列的长度


q.get(self,block=True,timeout=None)  获取队列的值

q.put_nowait()  不等 不阻塞
q.get_nowait()  不等 不阻塞

输入main  然后按Tab键  可以快速打出 if __name__ == '__main__':

'''

import time
from multiprocessing import Pool, Queue, Process
from random import random
import os

# def task(task_name):
#     print('开始做任务了！',task_name,os.getpid())
#     start = time.time()
#     time.sleep(random()*2)
#     end = time.time()
#     print('完成任务！用时{}：子进程{}，主进程{}'.format(end-start,os.getpid(),os.getppid()))
#     # return '完成任务！用时{},进程号{},主进程号{}'.format(end-start,os.getpid(),os.getppid())
#
# print('----分割线1------，进程号：',os.getpid())
# if __name__ == '__main__':
#     pool = Pool(5)
#
#
#     tasks = ['起床','刷牙','叠被子','做饭','吃饭','洗碗','听音乐','拖地板']
#     for task1 in tasks:
#         pool.apply(task,args=(task1,))   #添加阻塞式进程  无async 异步  无callback回调函数
#
#
#     pool.close()    #添加任务结束
#     pool.join()     #子进程没结束卡住，不让主进程继续往下，在pool 如果主进程结束，子进程就结束了
#
#     print('任务结束！')

print('----分割线进程间的通信1----')
q = Queue(5)  #队列
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E') #因为Queue(5) 最多是5个，所以如果超过的话 下面那个F就一直放不进去只能等待，直至空间让出来
print(q.qsize())
if q.full():  #判断队列是否满了
    print('队列已满')
else:
    q.put('F', timeout=3)  # 表示阻塞3秒钟，如果还没有空间就报异常

while not q.empty():
    print(q.get(timeout=2))
else:
    print('队列空了')

print('----分割线进程间的通信2----')

def download(q,b):
    for i in b:
        q.put(i)
        print('正则下载{}'.format(i))

def getfile(q):
    while True:
        try:
            file = q.get(timeout=3)
            print('下载完成{}'.format(file))
        except:
            print('打印完成')
            break

lists = ['boy.jpg','girl.jpg','man.jpg']
q = Queue(5)

if __name__ == '__main__':
    p1 = Process(target=download,args=(q,lists))
    p2 = Process(target=getfile,args=(q,))
    p1.start()
    p1.join()  #p1插队先做完,如果没有这个 p1进程结束 进程内部的变量就收回了

    p2.start()
    p2.join()

    print('任务完成！')



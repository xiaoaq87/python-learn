'''
线程，有时被被为轻量进程(Lightweight Process,LWP),是程序执行流的最小单元。一个标准的线程由线程I
D,当前指令指针(PC),寄存器集合和堆栈组成。另外，线程是进程中的一个实体，是被系统独立调度和分
派的基本单位，线程自己不拥有系统资源，只拥有一点儿在运行中必不可少的资源，但它可与同属一个进程的
其它线程共享进程所拥有的全部资源。一个线程可以创建和撤消另一个线程，同一进程中的多个线程之间可以
并发执行。由于线程之间的相互制约，致使线程在运行中呈现出间断性。线程也有就绪、阻塞和运行三种基本
状态。就绪状态是指线程具备运行的所有条件，逻辑上可以运行，在等待处理机;运行状态是指线程占有处理
机正在运行;阻塞状态是指线程在等待一个事件（如某个信号量），逻辑上不可执行。每一个程序都至少有一
个线程，若程序只有一个线程，那就是程序本身
线程是程序中一个单一的顺序控制流程。进程内有一个相对独立的、可调度的执行单元，是系统独立调度和分
派CPU的基本单位指令运行时的程序的调度单位。在单个程序中同时运行多个线程完成不同的工作，称为多线
程.
多线程：多线程(英语：multithreading),是指从软件或者硬件上实现多个线程并发执行的技术。具有多线程
能力的计算机因有硬件支持而能够在同一时间执行多于一个线程，进而提升整体处理性能。具有这种能力的系
统包括对称多处理机、多核心处理器以及芯片级多处理(Chip-level multithreading)或同时多线程
(Simultaneous multithreading)处理器。在一个程序中，这些独立运行的程序片段叫作“线程”(Thread)
利用它编程的概念就叫作“多线程处理(Multithreading)”。具有多线程能力的计算机因有硬件支持而能够在同
时间执行多于一个线程(台湾译作“执行绪”)，进而提升整体处理性能
·优点：
(1)使用线程可以把占据长时间的程序中的任务放到后台去处理。
(2)用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度
条来显示处理的进度
(3)程序的运行速度可能加快
(4)在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况
下我们可以释放一些珍贵的资源如内存占用等等。

Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简
单的锁。
threading模块提供的其他方法：
·threading.currentThread(）:返回当前的线程变量。
·threading.enumerate(）:返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动
前和终止后的线程。
·threading.activeCount():返回正在运行的线程数量，与len(threading.enumerate（）有相同的结果。
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法：

线程的状态：

新建状态---start----就绪状态------在CPU的运行状态------运行结束状态
                        阻塞状态（sleep）

和进程一样，线程也有
线程.start
线程.join

线程会共享全局变量，这点与用Process建进程，但当数据量大的时候会出问题，这是PYTHON在底层运行时，当其中线程还没完成就阻塞，另外一个线程就接下去，导致出问题
为了解决这个问题可以加锁lock 只有一个线程执行完成，下一个线程才能开始执行，这样就保证了全局变量数据的安全性，缺点是效率变慢了
python底层只要用线程默认枷锁，这样就不能实现真正意义上的多线程；但当计算量很大的时候，底层就会把这锁释放了

共享数据才会有安全性问题，但底层默认加锁，当计算密集型时，虽然底层会把锁解开，但可以手动加上

GIL 全局解释器锁

线程：耗时操作的时候，比如爬虫、IO操作、下载图片；伪线程
进程：计算密集型，一般计算量很大的时候

共享数据
如果出现多个线程对某个数据进行修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
同步：线程一个一个的完成，效率会降低
使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire的方法和release方法，对于那些需要每次只允许一个线程的操作，可以将其操作放到
acquire和release方法之间
多线程的优势在于可以同时运行多个任务（至少感觉起来是这样），但是当线程需要共享数据时，可能存在数据不同步的问题，为了避免这种情况，引入了锁的概念

lock = threating.Lock() 建立锁对象

lock.acquire() 请求得到锁
lock.release() 释放锁
只要不释放其他线程都无法进来


死锁
开发过程中使用线程，在线程间共享多个资源的时候
如果两个线程分别占用一部分资源并且同时等待对方的资源，就会造成死锁
尽管死锁很少发生，但一旦发生就会导致应用的停止响应，程序不做任何事

'''


import threading
import time
from time import sleep


def download(n):
    lists = ['壮志凌云','哪吒魔童闹海','封神榜']
    for i in lists:
        sleep(n)
        print('正在下载：{}'.format(i))

def listenMusic():
    musics = ['画','爱，很简单','苹果香']
    for music in musics:
        sleep(1)
        print('正在听歌：{}'.format(music))

if __name__ == '__main__':
    t1 = threading.Thread(target=download,name='下载',args=(1,))
    t1.start()
    t2 = threading.Thread(target=listenMusic,name='听歌')
    t2.start()


print('----分割线--------')

lock = threading.Lock()
list1 = [0]*10
def task1():
    lock.acquire()
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print('------:',i)
        time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(list1)
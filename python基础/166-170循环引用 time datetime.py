'''
1、循环导入
问题：模块之间相互引用导入
解决办法：避免相互导入
（1）重新架构  成本很高
（2）将导入的语句放在函数里
（3）把导入语句放在模块的最后
2、搜索顺序
当你导入一个模块，python解析器对模块位置的搜索顺序是：
（1）当前目录
（2）如果不在当前目录，python则搜索在shell变量pythonpath下的每个目录
（3）如果都找不到，python会查看默认路径 unix下 默认路径一般为/user/local/lib/pyhton/.
模块搜索顺序路径存储在system模块的sys.path变量中。变量里包含当前目录，pythonpath和由安装过程决定的默认路径

系统模块
3、sys

4、time

5、datetime  time模块升级版
    time   时间
    date   日期
    datetime  日期 时间
    timedelta 时间差




'''
import datetime
import sys
import time

print(sys.path)  # 搜索路径
print(sys.version)
print(sys.argv)  # 运行程序时的参数，argv 是一个列表

print('--------分割线 time---------')

t1 = time.time()  # 时间戳
print(t1)
for i in range(1000):
    pass

t2 = time.time()  # 时间戳
print(t2)

time.sleep(1)  # 延迟执行

s = time.ctime(t1)  # 时间格式转换为字符串格式
print(s)
print(type(s))

s1 = time.localtime(t1)  # 时间格式转换为元组格式
print(s1)
print(type(s1))
print(s1.tm_year)    #元组格式方便取里面的值

s2 = time.mktime(s1)  # 将元组格式转换为时间戳格式
print(s2)

s3 = time.strftime('%Y-%m-%d %H:%M:%S')  # 将元组格式s1转换为字符串特定时间格式，默认取当前时间戳
print(s3)

r = time.strptime('2019/06/20','%Y/%m/%d')  #格式转换
print(r)

print('--------分割线 datetime---------')

timedel = datetime.timedelta(days=1,hours= 2)
print(timedel)

now = datetime.datetime.now()  #得到当前日期时间
print(now)
result = now +timedel
print(result)
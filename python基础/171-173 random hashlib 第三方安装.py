'''

chr(数字)  可以获得包括字母内的  可以查看ASCII码对照表 65-90是大写字母
ord()   可以获得unicode码  刚好和上面相反

加密算法
不可逆：md5 sha1 sha256
可逆：base64

第三方 pillow 图片处理模块
pycharm  终端-本地 terminal-local  安装第三方库
也可以在运行安装第三方库
'''
import random
import hashlib

ran = random.random()  #0-1之间随机小数
print(ran)

ran = random.randrange(1,10,2) #一定期间的随机数，可设定步长
print(ran)

ran = random.randint(1,10)
print(ran)

list1 = ['张三','李四','王五']
ran = random.choice(list1)
print(ran)

pai = ['张三','李四','王五']
random.shuffle(pai)  #打乱顺序不返回值
print(pai)

def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0,9))
        ran2 = chr(random.randint(65, 90))  #随机获得大写字母
        ran3 = chr(random.randint(97, 122)) #随机获得小写字母

        r = random.choice([ran1,ran2,ran3])

        code +=r
    return code

result = func()
print(result)

print('------分割线chr-------')

print(chr(65))
print(ord('A'))
print(ord('上'))
print(chr(19978))

print('------分割线hashlib-------')

msg = '于鹏中午一起吃饭去！'
md5 = hashlib.md5(msg.encode('utf-8'))   #不能传入字符串，要按utf-8编码
print(md5)  #按二进制显示
print(md5.hexdigest())  #按十六进制显示

sha1 = hashlib.sha256(msg.encode('utf-8'))
print(sha1.hexdigest())



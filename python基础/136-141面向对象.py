
'''
面向对象：
类 对象 属性  方法

所有的类名首字母大写，多个单词使用驼峰式命名
默认继承Object

1、定义类、属性、方法：
class 类名[(父类)]:
    属性
    方法
python 允许对象修改属性

2、创建对象：  通过类创建对象
    类目（）
注意区分类属性和对象属性；
可以动态创建修改对象属性，不管该属性在不在在类属性反映，如果；
先在对象属性找，没有再去类属性找；

若要该类属性要用类去找   类.属性

3、类的方法
种类：普通方法 类方法 静态方法 魔术方法
普通方法
    def 方法名(self[,参数，参数])
    方法调用  .方法

魔术方法
    def __方法名__()
    __init__(self) 里面的属性是创建对象的属性不是类的属性，不能用类.属性调用
'''

class Phone:
    brand = 'huawei'  #定义类属性

#使用类创建对象 类/对象的属性
yp = Phone()
print(yp)
print(yp.brand) #先去对象空间找是否有brand属性，如果没有就回去类找brand属性
yp.brand = 'iphone'  #对象属性   python可以修改对象的属性
print(yp.brand)
yp.age = 2      #动态创建对象属性，该属性不会作用反映到类属性上
print(yp.age)

feifei = Phone()
print(feifei)
print(feifei.brand)  #feifei的属性没有收到yp属性的修改影响

Phone.brand = '小米'  #修改类的brand属性
print(yp.brand)
print(feifei.brand)

#类中方法
class Phone1:
    def __init__(self,type):   #self 对象地址
        self.brand = 'xiaomi'   #类一开始没有该属性,动态在self空间创建属性，但类调用不了该属性，因为self是创建对象空间地址
        self.price = 4999
        self.type = type
        print("-----init")

    def call(self,food):
        print('self-----',self)  #self  对象本身传进去，谁调用把自身传进去
        print('正在电话')
        print('留言:',self.note,self.price,food)  #不能保证每个对象都有note属性，所有会出现阴影

phone1 = Phone1('mate80')

'''
1、查找空间Phone1
2、利用Phone1类，向内存申请一块一样的空间；
3、去Phone1中找有没有_init_，如果没有则将开辟的内存给对象phone1
4、如果有_init_，则会进入init_执行，执行完成将内存空间地址赋值给phone1
_init_(self) self是对象的内存空间地址

'''
phone1.note = '我是phone的note'  #动态新增对象的属性
print(phone1)
phone1.call('apple')


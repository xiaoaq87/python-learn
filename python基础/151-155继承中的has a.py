'''
继承

has a ：反映类之间包含的关系，一个类中使用了另外一种自定义类型

类型：
系统类型 str int float list等
自定义类型：自定义的类，都可以当作一种类型

str(类)  如果类中定义了__str__，则就等效于__str__内容


is a: 基类  父类

默认会继承父类Object
继承
（1）Student Employee Docetor ---Person
（2）继承的语法  class 类（父类）


isinstance(obj,type)  返回布尔值，判断对象类型

特点
（1）如果类中不定义__init__，调用父类的__init__
（2）如果类继承父类也需要定义自己的__init__，就需要在当前类的__init__调用父类的__init__
（3）如何调用父类的__init__
    super().__init__([参数])
    super(类名，对象）.__init__（[参数]）
    父类.__init__([参数])

（4）如果父类和子类都定义了相同名字的方法，默认搜索原则：先找当前类，再找父类
如果父类提供的方法不能满足子类的需求，就需要再子类中定义一个相同名字的方法，这样就相当于重写

（5）子类的方法调用父类的方法
如果是在父类方法的基础上再补充，则可以在子类定义相同名字的方法中调用父类的方法  super().父类方法([参数])





'''
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的车，速度：{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京藏高速', 12000)

audi = Car('奥迪', 120)

print(audi)

audi.get_time(r)

print('------分割线-------')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在跑步')

    def run(self):
        print(self.name + '正在跑步')


class Student(Person):
    def __init__(self,name,age,clozz):    #如果子类要定义__init__，则需要调用父类的__init__，并且关注如果有参数传入的name age
        # super().__init__(name,age)    #super()  父类对象,父类拥有name age属性，直接调用父类的属性就可以
        super(Student,self).__init__(name,age)   #和上面的效果相同 super()
        self.clozz = clozz            #Student类单独拥有的属性clozz
    def run(self):
        print('{}正在跑步'.format(self.name))


class Employee(Person):
    pass


class Doctor(Person):
    pass

s = Student('jack',12,'18班')
s.run()

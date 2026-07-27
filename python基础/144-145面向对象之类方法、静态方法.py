'''
1、类方法
类方法的定义需要装饰器 @classmethod
类方法中的参数不是一个对象而是类
类方法中可以使用类属性，不能使用对象属性
类中普通方法兄弟方法的调用，需要通过self.方法名（）；类方法不能使用普通方法，这和属性道理类似，没有传入self
2、类方法作用
因为只能访问类属性和类方法，可以在对象创建之前，如果需要可以完成一些动作或功能
3、私有化
类属性前面加双下划线，就会私有化，外界无法访问修改类的属性

4、静态方法
4.1与类方法类似 需要装饰器@staticmethod 没有参数cls传入，但可以有其他参数传入
静态方法的调用与类方法调用一样
4.2静态方法无需传入参数（cls self），
4.3只能访问类的属性和方法，但无法访问对象的属性和方法
4.4加载的时机与类方法一样
4.5类方法与静态方法
不同：
（1）装饰器不同
（2）类方法有参数，静态方法没有
相同
（1）只能访问类的属性和方法，但无法访问对象的属性和方法
（2）都可以通过类名调用访问
（3）都可以创建对象之前使用，他们都不依赖对象

普通方法与两者的区别
不同
（1）无装饰器
（2）依赖对象，每个普通方法都有self
（3）只有创建对象，才能调用普通方法



'''

class Dog:
    def __init__(self,nickname):
        self.nickname = nickname
    def run(self):               #依赖对象调用 有self
        print('{}在院子里跑来跑去!'.format(self.nickname))

    @classmethod   #定义为类方法
    def test(cls):  #类方法，不需要依赖对象
        print(cls)   #Dog 类
        # print(cls.nickname)   #会报错 类没有该属性，除非类有定义该属性

d = Dog('大黄')
d.run()
d.test()      #这是类方法，用对象调用时候，如果对象没有该方法，会去看类有没有该方法

Dog.test()    #类方法 可以使用类去调用


class Person:
    __age = 18

    def __init__(self,name):
        self.name = name

    def show1(self):
        print('------',Person.__age)
    @classmethod
    def update_age(cls):
        cls.__age = 20

    @classmethod
    def show2(cls):
        print('修改后的年龄',cls.__age)

    @staticmethod
    def test():
        print('静态方法')
        # print(self.name)     #会报错 类似类方法
        print(Person.__age)    #使用类属性，虽然没参数传入，但可以通过类名调用

# print(Person.__age)  #外界无法访问
Person.update_age()
Person.show2()
Person.test()
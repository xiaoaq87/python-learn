'''
面向对象三大特点
封装（就是私有化）、继承、多态

私有化不会被子类继承

引用父类初始化的方式：
super().__init__()
super(所在类名,self).__init__()
父类.__init__()




'''



class Person:
    def __init__(self,name):
        self.name = name
    def feed_pet(self,pet): #多态是传入不一定要限定特定类，python属于多态，如果要限定特定的类可以结合isinstance实现
        if isinstance(pet,Pet): #判断obj是不属于这个类或这个类的子类的对象，
            print('{}喜欢养宠物:{},昵称是{}'.format(self.name,pet.role,pet.nickname))
        else:
            print('不是宠物类型')
class Pet:
    role = 'Pet'
    def __init__(self,nickname,age):
        self.nickname = nickname
        self.age = age
    def show(self):
        print('昵称：{}，年龄：{}'.format(self.nickname,self.age))

class Cat(Pet):
    role = '猫'
    def catch_mouse(self):
        print('抓老鼠')
class Dog(Pet):
    role = '狗'
    def watch_house(self):
        print('抓老鼠')
class Tiger:
    def eat(self):
        print('太可怕了')

cat = Cat('花花',2)
dog = Dog('大黄',4)
person = Person('家伟')

person.feed_pet(cat)
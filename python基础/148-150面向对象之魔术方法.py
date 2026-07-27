'''
1、__str__
触发时机：当打印对象名，自动触发去调动__str__内容
注意：__str__要添加return，

魔术方法总结
（1）重点：__init__ __str__
（2）了解：
__new__ 开辟空间
__del__ 没有指针引用的时候会调用，大部分不会用
__call__ 把对象当函数用


2、私有化

封装
（1）私有化属性
（2）定义set（为了赋值）和get（为了取值）方法
__属性 属性私有化，访问范围仅仅限于类中
好处
1、隐藏属性不被外界随意修改
2、通过set函数也可以修改
    def set**(self,***):
3、对赋值的内容进行约束

3、开发中看到一些私有化处理：装饰器


print(yupeng.__dir__()) #与print(dir(yupeng))等效 查看定义的attribute

'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age

    def __str__(self):
        return '姓名是：'+self.name+str(self.age)

p =Person('jack',18)
print(p)  #会返回__str__的内容

print('----分界线----')

class Student:
    # __age = 18
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.__socre = 59
    def setAge(self,age):
        if age > 0 and age <=120:  #可以对赋值进行限制
            self.__age = age
        else:
            print('超出范围')
    def setName(self,name):
        if len(name) == 6:
            self.name = name
        else:
            print('名字不是6位')

    def getAge(self):
        return self.__age   #通过return返回


    def __str__(self):
        return '姓名：{}，年龄:{}，考试成绩{}'.format(self.__name,self.__age,self.__socre)

yupeng = Student('yupeng',18)
print(yupeng)
print(dir(Student))   #通过dir可以看到Student类定义的属性、方法等，也就是attribute
print(yupeng.__dir__()) #与print(dir(yupeng))等效
print(dir(yupeng))  #通过dir可以看到yupeng对象的的属性、方法等，也直接看不到私有化部分的属性，因为会在前面加上_类名
'''
定义的函数 属性，统称attribute
通过dir 可以看到attribute形成的列表
凡是dir显示的attribute都可以通过.调用
私有化属性其实底层是被调整了 _类名__私有属性，所以通过这个也是可以访问到
'''
yupeng.setAge(20)
print(yupeng)
print(yupeng._Student__age) #私有化属性其实底层是被调整了 _类名__私有属性，所以通过这个也是可以访问到；但不建议该方式访问
print(yupeng.getAge())

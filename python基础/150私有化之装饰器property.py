'''
开发中看到一些私有化处理：装饰器

print(s.__dir__())查看拥有的属性\方法
dir(s)       效果和上面一样
'''


class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # def getAge(self):
    #     return self.__age  # 通过return返回

    @property
    def age(self):
        return self.__age


    # def setAge(self, age):
    #     if age > 0 and age <= 120:  # 可以对赋值进行限制
    #         self.__age = age
    #     else:
    #         print('超出范围')


    @age.setter    #先有上面age，才有这个
    def age(self,age):
        if age > 0 and age <= 120:  # 可以对赋值进行限制
            self.__age = age
        else:
            print('超出范围')




    def __str__(self):
        return '姓名：{}，年龄:{}'.format(self.name, self.__age)

s = Student('peng',20)
s.name = 'xiaopengpeng'  #name 未私有化
print(s.name)

#私有化赋值
print(s.age)   #有了装饰器@property 就可以像非私有化属性一样去操作
print(s.__dir__())   #列表里面也有 ‘age’

s.age = 21  #有了装饰器 就可以像非私有化属性一样去操作
print(s.age)
print(s.__dir__())

# s.setAge(30)
# print(s.getAge())
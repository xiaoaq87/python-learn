'''
定义猫
'''

class Cat:
    type = '猫'
    def __init__(self,nickname,age,color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self,food):
        print('{}喜欢吃{}'.format(self.nickname,food))

    def catch_mouse(self,color,weight):
        print('{},抓了一只{}kg的，{}的大老鼠'.format(self.nickname,weight,color))

    def sleep(self,hour):
        if hour<5:
            print('乖乖！继续睡觉吧')
        else:
            print('赶快起床出去抓老鼠')

    def show(self):
        print('猫的详细信息')
        print(self.nickname,self.age,self.color)

cat1 = Cat('花花',2,'灰色')
cat1.catch_mouse('黑色',2)

cat1.show()
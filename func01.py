# 定义函数：生成随机数
import random


def generate_random(number):
    for i in range(number):
        ran = random.randint(1,20)
        print(ran)


print(generate_random)  # 輸出函數的内存空間地址
print(generate_random(3))


def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print(s)

    return inner_func


func1 = func(7, 8)
func2 = func(2, 8)

print(func)
print(type(func))
print(func1)
print(type(func1))
print(func2)

func1()
func2()

list1 = [1,2,3]
m = max(list1)

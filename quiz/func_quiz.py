# Quiz-13
print("Quiz 13")


def sign(num):
    if num > 0:
        print("Positive")
    if num < 0:
        print("Negative")
    else:
        print("Zero")


sign(0)


# Quiz-16
def sign(num):
    if num > 0:
        print("Positive")


sign(7)

# Quiz-29
print("Quiz 29")


def calc(arr=[3]):
    arr.append(2)
    return arr


print(sum(calc()) + sum(calc()))

# Quiz-31
print("Quiz 31")


def foo():
    try:
        print(1, end=' ')
    finally:
        print(2)


k31 = foo()
print(k31)

# Quiz-58
print("Quiz 58")


def func58(x):
    return x * 2


result = func58(2)
result = func58(result)
result = func58(result)
print(result)

# Quiz-59
print("Quiz 59")
a59 = 10


def func59():
    global a59
    a59 = 50


func59()
print(a59)

# Quiz-61
print("Quiz 61")


def func61(a, b=2, c=3):
    print(a, b, c)


func61(1, c=4)

# Quiz-63
print("Quiz 63")


def func63(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)
    print(type(args))


func63(1, 3, 4, 5, c=6, d=7)

# Quiz-65
print("Quiz 65")


def func65(a, b):
    return a + b


# print(func65(3,4,6))
print(func65(3, 4))

# Quiz-70
print("Quiz 70")


def func70():
    try:
        print("hello , in try")
        return
    finally:
        print("hello, in finally")


func70()

# Quiz-71
print("Quiz 71")


def func71():
    x71 = 10

    def inner_fun():
        nonlocal x71;
        x71 += 5

    inner_fun()
    print(x71)


func71()


# Quiz-75
print("Quiz 75")


def func75(x):
    if x == 0:
        return 0
    else:
        return x + func75(x-1)


print(func75(5))

# Quiz-78
print("Quiz 78")


def func78(a, b=2, c=3):
    print(a, b, c)


print(func78(c=1, a=3))

# Quiz-79
print("Quiz 79")

x79 = 10


def func79():
    global x79
    x79 = 30


func79()
print(x79)

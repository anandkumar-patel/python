
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
def func58 (x):
    return x*2

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
    print(a,b,c)

func61(1, c=4)

# Quiz-63
print("Quiz 63")
def func63(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)
    print(type(args))

func63(1,3,4,5, c =6, d=7)

# Quiz-65
print("Quiz 65")
def func65(a, b) :
    return a + b

#print(func65(3,4,6))
print(func65(3,4))

# Quiz-70
print("Quiz 70")
def func70():
    try:
        print("hello , in try")
        return
    finally:
        print("hello, in finally")

func70()
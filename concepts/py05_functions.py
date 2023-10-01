def my_first_func():
    print("I am learning python function")


print("out side of function, should get called before function call")

my_first_func()


def square_func(x):
    return x*x


print("function square return", square_func(11))
print("function square at memory ", square_func)


def func(x, y=0):
    print("value of x :", x)
    print("value of y :", y)


# here y will take as 0
func(11)

func(11, 12)

# we can reverse the order then we have to mention parameter explicitly.
func(y=2, x=12)

# this will give error-> TypeError: func() got an unexpected keyword argument 'b'
# func(x=2, b=12)

'''
In Python – *args and **kwargs. 
These make a Python function flexible so it can accept 
a variable number of arguments and keyword arguments, respectively.
'''

def func1(a, b,*args, **kwargs):
    print(a, b, args, kwargs)


func1(11, 12, 13, 14, 15, k=5)

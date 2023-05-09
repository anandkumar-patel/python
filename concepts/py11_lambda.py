"""
A lambda function can take any number of arguments,
but can only have one expression.
SYNTAX : lambda arguments : expression

Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous
function inside another function.

Say you have a function definition that takes one argument, and that
argument will be multiplied with an unknown number:

Use lambda functions when an anonymous function is
required for a short period of time.

"""

x = lambda a: a + 10
print("value of x ", x(5))


def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
my_tripler = myfunc(3)

print(my_doubler(11))
print(my_tripler(11))

"""
Python is considered to be a dynamically typed language because
based on the value provided to the variable,
the type will be assigned automatically.

Python supports following inbuilt data types :
01- int
02- float
03- complex

04- bool
05- str

06- bytes
07- bytearray

08- range
09- list
10- tuple
11- set
12- frozenset
13- dict

14- None
"""

print("int data type :")
x = 13
print("value of x", x)
print("type of x", type(x))

print("")
print("float data type :")
x = 13.5
print("value of x", x)
print("type of x", type(x))

print("")
print("complex data type :")
x = 1 + 2j
print("value of x", x)
print("type of x", type(x))

print("")
print("bool data type :")
x = False
print("value of x", x)
print("type of x", type(x))

print("")
print("str data type :")
x = "anand"
print("value of x", x)
print("type of x", type(x))

print("")
print("bytes data type :")
data = [20, 30, 40, 50]
b = bytes(data)
print("value of b", b)
print("type of b", type(b))

print("")
print("bytearray data type :")
data = [20, 30, 40, 50]
b = bytearray(data)
print("value of b", b)
print("type of b", type(b))

"""
bytes data type represents a sequence of byte values with in the range of 0-255. 
Difference between byte and bytearray is : 
    byte data type is immutable (once it is defined we can’t change it) where as 
    bytearray datatype mutable (we can change the values after defining).
"""

print("")
print("range data type :")
r = range(10)
r1 = range(0, 50)
r2 = range(0, 50, 10)
print("value of r", r)
print("type of r", type(r))
print("value of r1", r1)
print("type of r1", type(r1))
print("value of r2", r2)
print("type of r2", type(r2))

print("")
print("list data type :")
x = ['a', 'b', 'c', 'd']
print("value of x", x)
print("type of x", type(x))

print("")
print("tuple data type :")
x = ('a', 'b', 'c', 'd')
print("value of x", x)
print("type of x", type(x))

print("")
print("set data type :")
x = {'a', 'b', 'c', 'd'}
print("value of x", x)
print("type of x", type(x))

print("")
print("frozen set data type :")
x = {'a', 'b', 'c', 'd'}
fs = frozenset(x)
print("value of fs", fs)
print("type of fs", type(fs))

print("")
print("dict data type :")
x = {100: 'JAVA', 101: 'Python', 102: 'PHP'}
print("value of x", x)
print("type of x", type(x))

print("")
print("None data type :")


# If a variable or def, does not have any value in it, the default data type is None.
def sample():
    y = 23


print("value of sample", sample())
print("type of sample", type(sample()))

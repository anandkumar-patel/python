# Arithmetic Operators
x = 4
y = 5
print(x + y)

# Comparison Operators
x = 4
y = 5
print('x > y  is', x > y)

# Assignment Operators
num1 = 4
num2 = 5
print("Line 1 - Value of num1 : ", num1)
print("Line 2 - Value of num2 : ", num2)

# compound assignment operator
num1 = 4
num2 = 5
res = num1 + num2
res += num1
print("Line 1 - Result of + is ", res)

# Logical Operators
a = True
b = False
print('a and b is', a and b)
print('a or b is', a or b)
print('not a is', not a)

# Membership Operators
x = 4
y = 8
list1 = [1, 2, 3, 4, 5]
if x in list1:
    print("Line 1 - x is available in the given list")
else:
    print("Line 1 - x is not available in the given list")
if y not in list1:
    print("Line 2 - y is not available in the given list")
else:
    print("Line 2 - y is available in the given list")

# Identity Operators
x = 20
y = 20
if x is y:
    print("x & y  SAME identity")
y = 30
if x is not y:
    print("x & y have DIFFERENT identity")

# Operator precedence
v = 4
w = 5
x = 8
y = 2
z = (v + w) * x / y
print("Value of (v+w) * x/ y is ", z)

print("/ and // and % and ** example")
x = 9
y = 4
print('x/y : ', x / y)
print('x%y : ', x % y)
print('x//y : ', x // y)
print('x**y : ', x ** y)
"""
Difference between / and // :
The “/” operator always performs floating point arithmetic, 
hence it will always returns float values. 
Where as “//” operator can perform both floating point and integral arithmetic. 

If both arguments are int type then '/' returns int type, 
if any one of argument is float type then it returns float type.
"""

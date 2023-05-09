"""
What is Tuple in Python?
    A tuple is just like a list of a sequence of immutable python objects.
    The difference between list and tuple is that list are declared in square brackets and can be changed
    while tuple is declared in parentheses and cannot be changed. However,
    you can take portions of existing tuples to make new tuples.

"""

tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida')
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1[0])
tup2 = tup1
print(tup2[1:4])

# empty tuple, we can't assign any value
tup3 = ()
print(tup3)

# one element tuple
tup3 = (50,)  # if we don't give comma(,) in tuple definition then it will consider as normal variable.
print(type(tup3))

# Packing and Unpacking
x = ("Guru99", 20, "Education")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print("\nunpacked tuple : ")
print(company)
print(emp)
print(profile)

# Comparing tuples

# case 1
a = (5, 6)
b = (1, 4)
print("\n case 1 :")
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# case 2
print("\n case 2 :")
a = (5, 6)
b = (5, 4)
if (a > b):
    print("a is bigger")
else:
    print("b is bigger")

# case 3
print("\n case 3 :")
a = (5, 6)
b = (6, 4)
if (a > b):
    print("a is bigger")
else:
    print("b is bigger")

# case 4
print("\n case 4 :")
a = (5, 6)
b = (5, 4)
if (a == b):
    print("a and b are equal")
elif (a > b):
    print("a is bigger")
else:
    print("b is bigger")

# Tuples and dictionary
a = {'x': 100, 'y': 200}
b = a.items()
print(b)

# Slicing of Tuple
x = ("a", "b", "c", "d", "e")
print(x[2:4])

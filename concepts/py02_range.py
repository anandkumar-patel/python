"""
Syntax: range(start, stop, step)

Parameter:

    start: [ optional ] start value of the sequence
    stop: next value after the end value of the sequence
    step: [ optional ] integer value, denoting the difference between any two numbers in the sequence.

Return: Returns a range type object.

"""


# here range from 0 to 9 and increment by 1
print("here range from 0 to 9 and increment by 1")
for i in range(10):
    print(i, end=" ")


# here range from 2 to 9 and increment by 1
print()
print("here range from 2 to 9 and increment by 1")
r1 = range(2, 10)
for i in r1:
    print(i, end=" ")


# here range from 2 to 9 and increment by 3
print()
print("here range from 2 to 9 and increment by 3")

for i in range(2, 10, 3):
    print(i, end=" ")


# using a float number
print()
print("float number")
for i in range(3.8):
    print(i)

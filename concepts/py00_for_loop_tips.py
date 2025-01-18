# 1- don't use loops at all
print("# 1- don't use loops at all")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = 0
for num in numbers:
    result += num

print(result)
# best way
print("# best way")
print(sum(numbers))

print("# best way to get sum of all element's square")
print(sum(i**2 for i in numbers))

# 2- use enumerate
print("# 2- use enumerate")
numbers = [10, 20, 30, 40]
for idx in range(len(numbers)):
    print(idx, numbers[idx])
# best way
print("# best way")
for idx, val in enumerate(numbers):
    print(idx, val)

# best way
print("# best way")
for idx, val in enumerate(numbers, start=1):
    print(idx, val)

# 3- use zip
print("# 3- use zip")
num = [1, 2, 3, 4, 6]
alph = ["a", "b", "c", "d"]
# for idx in range(len(num)):
# print(num[idx], alph[idx])

print("# best way")
for val1, val2 in zip(num, alph):
    print(val1, val2)

# 4- Think lazy!  use generator
print("# 4- Think lazy!  use generator")
events = [("learn", 5), ("learn", 10), ("relaxed", 20), ("learn", 15)]
minute_studied = 0
for event in events:
    if event[0] == "learn":
        minute_studied += event[1]

print(minute_studied)

print("# best way")
study_times = (event[1] for event in events if event[0] == "learn")
minute_studied = sum(study_times)
print(minute_studied)

# 5- use itertools
print("# 5- use itertools")
print("5.1- islice")
lines = ["line1", "line2", "line3", "line4", "line5", "line6",
         "line7", "line8", "line9", "line10", "line11", "line12"]
for i, line in enumerate(lines):
    if i >= 5:
        break
    print(line)
print()

print("# best way")
from itertools import islice

# first_five_line = islice(lines, 5)
# first_five_line = islice(lines, 2, 5)
first_five_line = islice(lines, 1, 5, 2)
for line in first_five_line:
    print(line)
""" 3.10 version
print("5.2- pairwise")
from itertools import pairwise
data = "ABCDEFG"
for i in range(len(data)-1):
    print(data[i], data[i+1])

print("# best way")
for pair in pairwise(data):
    print(pair[0], pair[1])
"""
print("5.3- takewhile")
for item in [1, 2, 4, -1, 4, 1, 3]:
    if item >= 0:
        print(item)
    else:
        break

print("# best way")
from itertools import takewhile

items = takewhile(lambda x: x >= 0, [1, 2, 4, -1, 4, 1, 3])
for item in items:
    print(item)

# 6- use numpy
print("# 6- use numpy")
import numpy as np

vec_a = [1, 2, 3]
vec_b = [4, 5, 6]

result = 0
for val1, val2 in zip(vec_a, vec_b):
    result += val1 * val2;
print(result)

print("# best way")
result = np.dot(vec_a, vec_b)
print(result)

N = 100_100_100


def sum_python():
    return sum(range(N))


def sum_numpy():
    return np.sum(np.arange(N))


print(sum_python())
print(sum_numpy())
import timeit

print("sum python:", timeit.timeit(sum_python, number=1))
print("sum numpy:", timeit.timeit(sum_numpy, number=1))

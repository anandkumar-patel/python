x = [1, 2, 3]
y = [1, 2, 3]

print(x is y, x == y)

set1 = (1, 2, 3, 'on')
set2 = ("python", 'dev')
set3 = set1 + set2
set4 = set(set3)
print(set3)

import numpy as nm
a = [1,2,3]
b=[4,5,6]
c = nm.add(a, b)
print(c)

ls = [1,2,3,4,5]
new_ls =[x**2 for x in ls if x%2==0]
print(new_ls)

def my_fun():
    for i in range(22,23,24):
        print(i)

my_fun()

def mul(y, x=10):
    return x*y

print(mul(15))

for index in range(20, 10, -3):
    print(index, end=' ')
print()
for index in range(1**2, 2**3):
    print(index, end=' ')



# Quiz-01
print("Quiz 01")
x1 = 2
y1 = 10
# x1 *= y1 * x1 + 1
x1 = x1*y1 * x1 + 1
print(x1, y1)

# Quiz-02
print("Quiz 02")
print("1 or 3 : ", 1 or 3)
print("1 and 3 : ", 1 and 3)
print("0 and 2 and 1 : ", 0 and 2 and 1)
print("0 and 2 or 1 : ", 0 and 2 or 1)
print("0 and 2 or 1 or 4 : ", 0 and 2 or 1 or 4)
print("0 or False and 1 : ", 0 or False and 1)

# Quiz-04
print("Quiz 04")
x4 = 1
if x4 == 1:
    print("Wow")
elif x4 < 2:
    print("Wow again!")
else:
    print("No wow!")

# Quiz-05
print("Quiz 05")
print(bool(' ') + 4)

# Quiz-14
print("Quiz 14")
n14 = ['123']
print('A_'.join(n14))

# Quiz-20
print("Quiz 20")
n20 = 5
while n20:
    n20 = n20 - 1
    print(n20, end=' ')
print()

# Quiz-23
print("Quiz 23")
print(1, 2, 3, 4, 5, sep=',', end='.')
print()

# Quiz-24
print("Quiz 24")
a24 = 4
if a24 < 0:
    print("Negative")
print(a24)

# Quiz-28
print("Quiz 28")
for i in zip((1, 3, 5, 7, 9)):
    print(i, end=' ')
print()

# Quiz-38
print("Quiz 38")
for i, v in enumerate(['s', 'h', 'i', 'n', 'e']):
    print(i, v, sep="_", end=';')
print()

# Quiz-47
print("Quiz 47")
x47 = 10
y47 = 20
_ = x47 + y47
print(_)

# Quiz-48
print("Quiz 48")
a48, *b48 = 10, 20, 30
print(type(b48))

# Quiz-49
print("Quiz 49")
print(1, 2, 3, 4, 5, sep='-', end='.')

# Quiz-83
print("Quiz 83")
x = 5
y = 10
result83 = (x > y) or (y < 2) and (y == 10)
print(result83)

# Quiz-86
print("Quiz 86")
x86 = 10
y86 = 2
result86 = x86%y86 == 0
print(result86)

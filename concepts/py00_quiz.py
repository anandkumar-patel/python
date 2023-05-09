from statistics import median

# Quiz-01
print("Quiz 01")
x1 = 2
y1 = 10
x1 *=y1*x1+1
print(x1, y1)

# Quiz-02
print("Quiz 02")
print("1 or 3 : ", 1 or 3)
print("1 and 3 : ", 1 and 3)
print("0 and 2 and 1 : ", 0 and 2 and 1)
print("0 and 2 or 1 : ", 0 and 2 or 1)
print("0 and 2 or 1 or 4 : ", 0 and 2 or 1 or 4)
print("0 or False and 1 : ", 0 or False and 1)
# Quiz-03
print("Quiz 03")
li3 = "python".split(" ")
print(li3)

# Quiz-04
print("Quiz 04")
x4 = 1
if  x4 == 1:
    print("Wow")
elif x4 < 2:
    print("Wow again!")
else:
    print("No wow!")

# Quiz-05
print("Quiz 05")
print(bool(' ')+4)

# Quiz-06
print("Quiz 06")
s = set()
# un-comment
# print(s.pop())

# Quiz-07
print("Quiz 07")
s7 = "Beginning"
print(s7.replace('n', 'N',-1))

# Quiz-08
print("Quiz 08")
li8 = ['A']
li8.extend('BCD')
print(li8)

# Quiz-09
print("Quiz 09")
s8 = {2, 3, 1, 6, 9}
s9 = {1, 3, 5, 7}
print(s8^s9)


# Quiz-10
print("Quiz 10")
s10 = 'chocolate'
print(s10.replace('o', 'p'))

# Quiz-11
print("Quiz 11")
list11 = [1, 2, 3, 4, 5, 6]
print(5.0 in list11, end=" ")
print('5' in list11)

# Quiz-12
print("Quiz 12")
s12 = 'amazing'
# un-comment
# print(s12.index('a', 2, 2))

# Quiz-13
print("Quiz 13")
def sign(num):
    if num>0:
        print("Positive")
    if num<0:
        print("Negative")
    else:
        print("Zero")

sign(0)
# Quiz-14
print("Quiz 14")
n14 = ['123']
print('A_'.join("B"))

# Quiz-15
s14 = {5, 10, 20, 30}
s15 = {20, 25, 35}
s14.intersection_update(s15)
print(s14)

# Quiz-16
def sign(num):
    if num>0:
        print("Positive")

sign(7)

# Quiz-17
list17 = [5,'t', 5.6, 32, 'PythonGeeks']
print(3.0 in list17, end=" ")
print(bool(list17[-2:-4]))

# Quiz-18
print("Quiz 18")
s18 = "programming"
print(s18.partition('r'))

# Quiz-19
print("Quiz 19")
s19 = 'Python Possibilities'
print(s19.partition('p'))

# Quiz-20
print("Quiz 20")
n20 = 5
while n20:
    n20 = n20 - 1
    print(n20, end=' ')
print()

# Quiz-21
print("Quiz 21")
a21 = {'name':'abc'}
b21 = a21
c21 = a21.copy()
a21['name'] = 'xyz'
print(b21['name'], c21['name'])

# Quiz-22
print("Quiz 22")
import string as s22
s22 = {c22 for c22 in s22.ascii_lowercase if c22 in 'aeiou'}
print(s22)

# Quiz-23
print("Quiz 23")
print(1,2,3,4,5, sep=',', end='.')
print()

# Quiz-24
print("Quiz 24")
a24 = 4
if a24<0:
    print("Negative")
print(a24)

# Quiz-25
print("Quiz 25")
s25 = {3,2,6,7,2,5,3,1,-1,4}
n25 =[val for val in s25 if val%2 !=0]
print(len(n25))
print(n25)

# Quiz-26
print("Quiz 26")
s24 = {'c', 'b', 'd'}
s26 = {'c', 'b', 'd'}
print(s26<= s24)

# Quiz-27
print("Quiz 27")
s27 = "linkedin"
print(s27.replace("in", "is"))

# Quiz-28
print("Quiz 28")
for i in zip((1,3,5,7,9)):
    print(i, end=' ')
print()

# Quiz-29
print("Quiz 29")

def calc(arr = [3]):
    arr.append(2)
    return arr

print(sum(calc()) + sum(calc()))

# Quiz-30
print("Quiz 30")
li30 = [10, 20, 30, 40]
li30[1:3] = [50]
print(li30)



# Quiz-38
print("Quiz 38")
for i, v in enumerate(['s','h','i','n','e']):
    print(i,v, sep="_", end= ';')
print()

# Quiz-39
print("Quiz 39")
# x39 = str(2)+int(2.0)+float(3)
# print(x39)



# Quiz-42
print("Quiz 42")
ls41 = {2,3,1,6,9}
ls42 = {1,3,5,7}
print(ls41^ls42)


# Quiz-47
print("Quiz 47")
x47 = 10
y47 = 20
_ = x47+y47
print(_)

# Quiz-48
print("Quiz 48")
a48, *b48 = 10, 20, 30
print(type(b48))

# Quiz-49
print("Quiz 49")
print(1,2,3,4,5, sep='-', end= '.')


# Quiz-50
print("\nQuiz 50")
li50 = ['in', 'as', 'if', 'be']
print(li50[1:][:2])

# Quiz-51
print("Quiz 51")
li51 = [11, 12, 13, 14, 15]
print(li51[slice(1, 4)])

# Quiz-52
print("Quiz 52")
li51 = (1, 2, 3)
li52 = ('i', 'ii', 'iii')
print(list(zip(li51,li52)))

# Quiz-53
print("Quiz 53")
li53 = ['W']
li53.extend('XYZ')
print(li53)

# Quiz-54
print("Quiz 54")
z54 = ('z', 'i', 'p')
z55 = ()
print(list(zip(z54, z55)))

# Quiz-55
print("Quiz 55")
l55 = [-33, 23, 45, 3, 30, 203]
print(list(filter(lambda n: n%10 ==3, l55)))

# Quiz-56
print("Quiz 56")
t56 = (15, 5, 1, 7, 4, 10)
print(median(t56))

# Quiz-60
print("Quiz 60")
a60 = {1:'One', 2: 'two', 3: 'three'}
for key in a60:
    print(key,a60[key])

# Quiz-64
print("Quiz 64")
a64 = {1:'one', 2: 'two', 3: 'three',4:'four'}
b64 = {k: v for k,v in a64.items() if k%2 == 0}
print(b64)

# Quiz-66
print("Quiz 66")
for i in range(3):
    for j in range(3):
        print(i*j)




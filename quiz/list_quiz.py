# Quiz-08
print("Quiz 08")
li8 = ['A']
li8.extend('BCD')
print(li8)

# Quiz-11
print("Quiz 11")
list11 = [1, 2, 3, 4, 5, 6]
print(5.0 in list11, end=" ")
print('5' in list11)

# Quiz-17
list17 = [5, 't', 5.6, 32, 'PythonGeeks']
print(3.0 in list17, end=" ")
print(bool(list17[-2:-4]))

# Quiz-30
print("Quiz 30")
li30 = [10, 20, 30, 40]
li30[1:3] = [50]
print(li30)

# Quiz-35
print("Quiz 35")
li35 = [2, 3, 1]
print(li35.pop(1))

# Quiz-40
print("Quiz 40")
month40 = ['Feb', 'March']
print(list(enumerate(month40, start=2)))

# Quiz-41
print("Quiz 41")
li41 = [20, 40, 60]
li41.append(80)
print(li41.remove(20))

# Quiz-43
print("Quiz 43")
a43 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a43[-3:-1])

# Quiz-44
print("Quiz 44")
num44 = [2, 3, 4, 5]
print(sum(num44, 100))

# Quiz-45
print("Quiz 45")
x45 = [1, 2, 3]
y45 = x45
y45[1] = 4
print(x45)

# Quiz-46
print("Quiz 46")
num46 = [1, 'Python', -1, [], 9]
print(any(num46), all(num46))

# Quiz-50
print("\nQuiz 50")
li50 = ['in', 'as', 'if', 'be']
print(li50[1:][:2])

# Quiz-51
print("Quiz 51")
li51 = [11, 12, 13, 14, 15]
print(li51[slice(1, 4)])

# Quiz-53
print("Quiz 53")
li53 = ['W']
li53.extend('XYZ')
print(li53)

# Quiz-55
print("Quiz 55")
l55 = [-33, 23, 45, 3, 30, 203]
print(list(filter(lambda n: n % 10 == 3, l55)))

# Quiz-62
print("Quiz 62")
a62 = [1, 2, 3, 4, 5]
b62 = [i for i in a62 if i % 2 == 0]
print(b62)

# Quiz-67
print("Quiz 67")
x67 = [1, 2, 3]
y67 = x67
x67.append(4)
print(y67)

# Quiz-68
print("Quiz 68")
lst68 = [1, 2, 3, 4, 5]
for i in lst68:
    if i == 3:
        break
    else:
        print("Completed Successfully")

# Quiz-69
print("Quiz 69")
lst69 = [1, 2, 3, 4, 5]
new_lst69 = [i * i for i in lst69 if i % 2 == 0]
print(new_lst69)

# Quiz-73
print("Quiz 73")
li72 = [1, 2, 3, 4, 5]
# it will pop the last added element
print(li72.pop())


# Quiz-77
print("Quiz 77")
li77 = [1, 2, 3]
li78 = [4, 5, 6]
z77 = zip(li77, li78)
print(list(z77))

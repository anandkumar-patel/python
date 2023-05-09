
# Quiz-35
print("Quiz 35")
li35 = [2,3,1]
print(li35.pop(1))

# Quiz-40
print("Quiz 40")
month40 = ['Feb','March']
print(list(enumerate(month40, start=2)))

# Quiz-41
print("Quiz 41")
li41 = [20,40, 60]
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
num46 = [1, 'Python',-1,[],9]
print(any(num46), all(num46))


# Quiz-62
print("Quiz 62")
a62 = [1,2,3,4,5]
b62 =[i for i in a62 if i%2==0]
print(b62)

# Quiz-67
print("Quiz 67")
x67 = [1,2,3]
y67 = x67
x67.append(4)
print(y67)

# Quiz-68
print("Quiz 68")
lst68 = [1, 2, 3, 4, 5]
for i in lst68:
    if i ==3:
        break
    else:
        print("Completed Successfully")

# Quiz-69
print("Quiz 69")
lst69 = [1, 2, 3, 4, 5]
new_lst69 = [i*i for i in lst69 if i%2 ==0]
print(new_lst69)
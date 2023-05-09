import datetime
# 1 swap two variable without using temp
a = 10
print("swap two variable without using temp")
b = 15
print(a, b)
a, b = b, a
print(a, b)

# 2- list comprehension
squares = []
for i in range(10):
    squares.append(i*i)
print(squares)
# comprehensive way
squares = [i*i for i in range(10)]
print(squares)

# with condition
squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i*i)
print(squares)
# comprehensive way
squares = [i*i for i in range(10) if i % 2 == 0]
print(squares)

# 3- if else
a = 23
b = 45
c = 95 if a > b else 100
print(c)

# 4- print only elements of collection without new lines
data = [1, 2, 3, 4, 5, 6]
# here it prints list bracket
print(data)
for i in data:
    print(i, end=" ")
print()
print("here after print() it's going in new line")

# one liner
print(*data)


# 5- days left in a calendar year

print((datetime.date(2022, 12, 31) - datetime.date.today()).days)


# 6- reverse a list
list_data = [1, 2, 3, 4, 5, 6, 7]
print(list_data)
reversed_list = list_data[::-1]
print(reversed_list)

# 6.2- reverse a string

str_data = "anand kumar"
reversed_str_data = str_data[::-1]

print(str_data)
print(reversed_str_data)

# 6.3- checking a palindrome
str_data = "level"
print(str_data == str_data[::-1])


# 7- multiple variable assignment
name, age, sex = "anand", 35, "male"
print(name, age, sex)

# 8- space separated number string to integer list
user_input = "1 2 3 4 5 6"
my_list1 = user_input.split()
print(my_list1)
my_list2 = list(map(int, user_input.split()))
print(my_list2)

# 9 reading file into list
names = [line.strip() for line in open("py00_best_one_liner.txt", "r")]
print(names)

# Quiz-06
print("Quiz 06")
s = set()
# un-comment
# print(s.pop())

# Quiz-09
print("Quiz 09")
s8 = {2, 3, 1, 6, 9}
s9 = {1, 3, 5, 7}
print(s8 ^ s9)

# Quiz-15
print("Quiz 15")
s14 = {5, 10, 20, 30}
s15 = {20, 25, 35}
s14.intersection_update(s15)
print(s14)

# Quiz-25
print("Quiz 25")
s25 = {3, 2, 6, 7, 2, 5, 3, 1, -1, 4}
n25 = [val for val in s25 if val % 2 != 0]
print(len(n25))
print(n25)

# Quiz-26
print("Quiz 26")
s24 = {'c', 'b', 'd'}
s26 = {'c', 'b', 'd'}
print(s26 <= s24)

# Quiz-42
print("Quiz 42")
ls41 = {2, 3, 1, 6, 9}
ls42 = {1, 3, 5, 7}
print(ls41 ^ ls42)

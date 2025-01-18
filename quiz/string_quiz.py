import string as s

# Quiz-01
print("Quiz 01")
li1 = "python".split(" ")
print(li1)

# Quiz-02
print("Quiz 02")
s2 = "Beginning"
print(s2.replace('n', 'N', -1))

# Quiz-03
print("Quiz 03")
s03 = 'chocolate'
print(s03.replace('o', 'p'))

# Quiz-04
print("Quiz 04")
s4 = 'amazing'
# un-comment
# print(s4.index('a', 2, 2))

# Quiz-05
print("Quiz 05")
s5 = "programming"
print(s5.partition('r'))

# Quiz-06
print("Quiz 06")
s6 = 'Python Possibilities'
print(s6.partition('p'))

# Quiz-07
print("Quiz 07")

s7 = {c7 for c7 in s.ascii_lowercase if c7 in 'aeiou'}
print(s7)

# Quiz-08
print("Quiz 08")
s8 = "linkedin"
print(s8.replace("in", "is"))

# Quiz-09
print("Quiz 09")
s9 = '\n'
print(s9.split(), s9.splitlines())

# Quiz-10
print("Quiz 10")
s10 = "abcde"
print(s10.split('c'))

# Quiz-11
print("Quiz 11")
s11 = "awesome"
print(s11.replace('e', 'r', 1))

# Quiz-12
print("Quiz 12")
s12 = "coding"
print(s12[10: 0: -1])

# Quiz-13
print("Quiz 13")
# x13 = str(2)+int(2.0)+float(3)
# print(x13)

# Quiz-14
print("Quiz 14")
s14 = "Hello, World!"
print(s14[:5])
print(s14[7:])

# Quiz-15
print("Quiz 15")


def modify_str():
    str15 = 'I love python'
    str15.replace('love', 'like').split()
    return str15


print(modify_str())

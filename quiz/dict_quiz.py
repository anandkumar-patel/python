# Quiz-21
print("Quiz 21")
a21 = {'name': 'abc'}
b21 = a21
c21 = a21.copy()
a21['name'] = 'xyz'
print(b21['name'], c21['name'])

# Quiz-34
print("Quiz 34")
d34 = dict(A=65,B=66, C=67)
print(d34)

# Quiz-60
print("Quiz 60")
a60 = {1: 'One', 2: 'two', 3: 'three'}
for key in a60:
    print(key, a60[key])

# Quiz-64
print("Quiz 64")
a64 = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
b64 = {k: v for k, v in a64.items() if k % 2 == 0}
print(b64)


# Quiz-74
print("Quiz 74")
dict74 = {"a": 1, "b": 2, "c": 3}
print(dict74.keys())

# Quiz-76
print("Quiz 76")
dict74 = {"a": 1, "b": 2, "c": 3}
for keys, values in dict74.items():
    print(keys, values)

# Python input read input from keyboard
rawInput = input("Enter your name : ")
print(rawInput)
print(type(rawInput))
print("")

# string
var1 = "anand patel!"
var2 = "Software developer"
# index based character print
print("var1[0]:", var1[0])
# index based slice of string and print
print("var2[1:5]:", var2[1:5])
print("")

# in and not in -- java equivalent to contains()
x = "data science "
print("d" in x)
print("d" not in x)
print("j" in x)
print("j" not in x)
print('')

y = " and technology"
# concatenate the string
print(x + y)
# Repeat the string
print(2 * x)

print('')
# replace worlds
old_string = 'I like watching movies'
new_string = old_string.replace('like', 'love')
print(new_string)

print('')
# upper/lower/capitalize/title
string1 = "python learning"
print(string1.upper())
string2 = "ANAND KUMAR PATEL"
print(string2.lower())
print(string1.capitalize())
print(string2.capitalize())
print(string1.title())
print(string2.title())
print("")

# string join method.
"""
The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.
SYNTAX : separator_string.join(iterable)
"""
print("join example")
print(":".join("Python"))
myTuple = ("John", "Peter", "Vicky")

x2 = "#".join(myTuple)
print(x2)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "_"

print("******* joining the dictionary ********")
x3 = mySeparator.join(myDict)
print(x3)

print("******* joining the dictionary keys ********")
x4 = mySeparator.join(myDict.keys())
print(x4)

print("******* joining the dictionary values ********")
x5 = mySeparator.join(myDict.values())
print(x5)

# reverse the string
string1 = "12345"
print(''.join(reversed(string1)))

#  split the string
word = "guru99 career guru99"
print(word.split(' '))

# returns list
data1 = word.split(' ')
print(type(data1))

# string is immutable in python
x = "anand kumar patel anand"
y = x.replace("anand", "surya")
print(x)
print(y)

def main():
    print("hello python world!")


main()

print("normal print")

print('\n')
# Python input read input from keyboard
# rawInput=input("Enter any value : ")
# print(rawInput)
# print(type(rawInput))

print('\n')
# string
var1 = "anand patel!"
var2 = "Software developer"
# index based character print
print("var1[0]:", var1[0])
# index based slice of string and print
print("var2[1:5]:", var2[1:5])

# in and not in -- java equivalent to contains()
print('\n')
x = " data science "
print("d" in x)
print("d" not in x)
print("j" in x)
print("j" not in x)

print('\n')
y = " and technology"
# concatenate the string
print(x + y)
# Repeat the string
print(2 * x)

print('\n')
# replace worlds
oldstring = 'I like watching movies'
newstring = oldstring.replace('like', 'love')
print(newstring)

print('\n')
# upper/lower/capitalize
string1 = "python learning"
print(string1.upper())
string2 = "ANAND KUMAR PATEL"
print(string2.lower())
print(string2.capitalize())
print(string1.capitalize())

# string join method.
"""
The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.
"""
print("\njoin example")
print(":".join("Python"))
myTuple = ("John", "Peter", "Vicky")

x2 = "#".join(myTuple)
print(x2)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x3 = mySeparator.join(myDict)
print(x3)

x4 = mySeparator.join(myDict.values())
print(x4)

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
x = "anand"
x.replace("anand", "Python")
print(x)

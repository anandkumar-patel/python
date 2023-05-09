"""
Python Number Systems :
The python number system is representing the way of using the below numbers in Language.

    1- Binary Number System         : should start with 0b
    2- Octal Number System          : should start with 0o (zero and alphabet o)
    3- Decimal Number System        : can give value between 0-9
    4- Hexadecimal Number System    : should start with 0x
"""

print("converting to  binary :")
# Decimal to binary using bin()
data1 = 25
print('Decimal :', data1, ' and Binary :', bin(data1))
# Octal to binary using bin()
data2 = 0o127
print(bin(data2))
# Hexadecimal to binary using bin()
data3=0x235f
print(bin(data3))

print("converting to  int :")
# String to int
data4 = "150"
print(int(data4))
# floating point String to int
data5 = "15.15"
data6 = float(data5)
print(int(data6))


print("input from keyboard")
data = int(input("Please enter any number :"))
print(type(data))
data1 = float(input("Please enter any number :"))
print(type(data1))

print("# How to read multiple values from the keyboard in a single line")
x, y = [int(a) for a in input("Enter any 2 numbers :").split()]
print("Product of given two numbers -: ", x*y)

x, y, z = [float(a) for a in input("Enter any 3 numbers :").split(',')]
print("Sum of given three numbers -: ", x+y+z)

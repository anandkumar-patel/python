"""
Note:
    Python does not have built-in support for Arrays,
    but Python Lists can be used instead.

REFER LIST FOR ALL METHODS

"""

cars = ["Ford", "Volvo", "BMW"]

# length of array
x = len(cars)
print(x)
print(type(cars))

# looping the array
for x in cars:
    print(x)

# adding an element to array
cars.append("Honda")
print("after appending an element :")
print(cars)

cars.pop()
print(cars)

cars.pop(0)
print(cars)

cars.remove("Volvo")
print(cars)

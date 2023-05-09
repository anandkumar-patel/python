"""
Dictionaries are another example of a data structure.
A dictionary is used to map or associate things you want to store the keys you need to get them.
A dictionary in Python is just like a dictionary in the real world.
Python Dictionary are defined into two elements Keys and Values.

Keys will be a single element
Values can be a list or list within a list, numbers, etc.

Syntax for Python Dictionary:

Dict = { ' Tim': 18,  xyz,.. }

Properties of Dictionary Keys

There are three important points while using dictionary keys

1- More than one entry per key is not allowed ( no duplicate key is allowed)
2- The values in the dictionary can be of any type while the
   keys must be immutable like numbers, tuples or strings.
3- Dictionary keys are case-sensitive Same key name but with the different case are
   treated as different keys in Python dictionaries.

Here is the list of all Dictionary Methods

    Method	        Description	                                                            Syntax
    copy()	        Copy the entire dictionary to new dictionary	                        dict.copy()
    update()	    Update a dictionary by adding a new entry or a key-value pair to an
                    existing  entry or by deleting an existing entry.	                    dict.update([other])
    items()	        Returns a list of tuple pairs (Keys, Value) in the dictionary.	        dictionary.items()
    sort()	        You can sort the element	                                            dictionary.sort()
    len()	        Gives the number of pairs in the dictionary.	                        len(dict)
    str()	        Make a dictionary into a printable string format	                    str(dict)

"""
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print(Dict['Tiffany'])

print("Copying dictionary :")
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
studentX = Boys.copy()
studentY = Girls.copy()
print(studentX)
print(studentY)

print("updating the dictionary :")
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("original :", Dict)
Dict.update({"Sarah": 9})
print("updated :", Dict)

print("dictionary items method :")
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("Students Name: %s" % Dict.items())

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:
        print(False)

for data in list(Dict.keys()):
    print(data)

for data in list(Dict.values()):
    print(data)

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("variable Type: %s" % type(Dict))

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("printable string:%s" % str(Dict))
print("dict print :%s" % Dict)

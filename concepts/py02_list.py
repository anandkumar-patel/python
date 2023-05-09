'''
Characteristics of List :
    1-  Python List is a mutable sequence of characters, typically used to store collections of similar items.
    2-  List preserves the Insertion order.
    3-  Python List allows duplicate elements.
    4-  Python List is mutable, i.e. once we create a list, it can be modified at any time.
    5-  Python List is considered to be a dynamic because based on our requirement it will grow and shrink in size.
    6-  We can traverse the list in both the directions that are left to right and right to left.
    7-  Since the Python List is an index based data structure, we can traverse the list by using indexes.
    8-  A positive index can be used to traverse from left to right, and a
        negative index used to traverse from right to left.
        for positive it's [0 TO n] and for negative it's [-1 TO -n], -1 means last element.

Deleting Elements from a List :
    You can remove the list elements in two different ways.

    1-  remove() function is used to remove the list element by value.
    2-  del keyword is used to delete the list element by index.

Accessing List using slice (:):
    We can access the list elements like between the indexes.
    The slice operator helps us to read values from the list for a given index range.

    Syntax :

        list[start:end:step]
            Start – indicates that the index position, where the real slice has to start, the default value is 0.
            End – indicates that the index position, where the slicing has to end, the default value is the length of the list.
            Step – is an increment value; the default increment value is 1.

        Note: start includes the index value whereas end excludes the index value.

List inbuilt Functions :
    1-  len()
        len() function returns the number of elements present in the list.
    2-  count()
        The count() function returns the number of occurrences of the specified item in the list.
    3-  index()
        It returns the index of the first occurrence of the given item.
    4-  clear()
        The clear() function is used to clear the elements inside a list.
    5-  max()
        The max() function is used to get the max value from the list.

Manipulating List Elements:
    1-  append()
        append() function is used to add the item to the list at the end of the list.
    2-  insert()
        The insert() function is used to insert an item to the list at a given index position.

        Note: If the given index is greater than the max size of the list, then the element will be inserted
        at the last position. Similarly, if the specified index is smaller than the min size of the list,
        then the item will be added at first position.
    3-  extend()
        The extend() function is used to add all items in a list to another list at a time.

    4-  remove()
        remove() function is used to remove a specific item from the list.
        If the specified item found in multiple times, then it will remove the first occurrence.

    5-  pop()
        pop() function is used to remove the last element of the list and returns the popped item.
        pop(index) function is used to remove the item based on the given index.

        NOTE- Usually, append, and pop functions are used to implement a stack data structure.

Ordering the List Elements :
    1-  reverse()
        The reverse() function is used to make the list elements in reverse order.
    2-  sort()
        In a list, by default insertion order is preserved, if we want to sort the elements of the list
        according to default natural order, then we can use the sort() method.

        If a List contains only numerical, the default natural sorting order will be Ascending order.
        If a List contains only strings, then the default natural sorting order will be Alphabetical order.
        sort() method apply on List if the List contains homogenous elements. Otherwise, it will give TypeError.

Note: Whenever we compare the list using comparison operators like (== and !=) the List object
considers the following scenarios to examine the elements.
    1-  The number of elements present in a list
    2-  The order of elements
    3-  The content of List (Case sensitivity)
    4-  The List can also be compared using relational operators (<,<=,> and >=).

In the case of relational operators, the comparison happens only on the first element of the list;
the remaining elements should be ignored.
'''

list = [10, 20, 50, 30, 60, 40]
print("Before Updation : ", list)
list[2] = "A"
print("After Updation : ", list)

print("Before remove : ", list)
list.remove(10)
print("After Deletion element 10 : ", list)

print("Before del : ", list)
del list[3]
print("After Deletion  3rd element : ", list)

print("# Obtaining List using the index :")
list = [10, 20, 50, 30, 40]
print(list[0])
print(list[-1])  # last element
print(list[-2])  # previous to last element
print(list[4])

print("# Accessing List using slice (:):")
list1 = (10, 20, 50, 30, 40, 60, 70, 80, 90)
print("Between 2 and 7 indexes increment by 1 : ", list1[2:7:1])
print("Between 2 and 7 indexes increment by 2 : ", list1[2:7:2])
print("Between 2 and 7 indexes : ", list1[2:7])

print("# Traversing List using Loops :")
list = [10, 20, 50, 30]

print("# Using For loop")
for i in list:
    print(i)
print("#Using while loop")
i = 0
while i < len(list):
    print(list[i])
    i = i + 1
print("len function")
list = [10, 20, 50, 30, 40, 60, 70, 80, 90]
print("Length of the list : ", len(list))

print("count function")
list = [1, 2, 4, 3, 3, 5, 5, 6, 3, 9, 99, 8]
print("count the 3 :", list.count(3))
print("count the 5 :", list.count(5))
print("count the 9 :", list.count(9))

print("index function")
print(list.index(2))

print("max function :")
print(max(list))

print("append function :")
list.append(32)
print(list)

print("insert function :")
list.insert(1, 34)
print(list)

print("extend function")
list = ['o', 'n', 'l', 'i', 'n', 'e']
list2 = ['t', 'u', 't', 'o', 'r', 'i', 'a', 'l', 's']
list3 = ['p', 'o', 'i', 'n', 't']
list.extend(list2)
list.extend(list3)
print(list)

print("remove function")
list = [10, 20, 30, 40, 10, 20]
list.remove(20)
# list.remove(2) # ValueError: list.remove(x): x not in list

print("pop function")
print(list)
print(list.pop())

print(list)
# pop index based
print(list.pop(2))
print(list)

print("# Aliasing and Cloning of List Object :")
list1 = [10, 20, 30, 40, 50]
list2 = list1
print("id of list1", id(list1))
print("id of list2", id(list2))

print("List Cloning using slice operator :")
list2 = list1[:]
list1[1] = 123

print("list1 :", list1)
print("list2 :", list2)

print("List Cloning using copy() function: ")
list1 = [10, 20, 30, 40, 50]
list2 = list1.copy()
list1[1] = 100
print(list1)
print(list2)

print("How to compare two Lists:")
list1 = ['APPLE', 'BANANA', 'GRAPES']
list2 = ['APPLE', 'BANANA', 'GRAPES']
list3 = ['Apple', 'Banana', 'Grapes']

print(list1 == list2)
print(list1 == list3)
print(list1 != list3)

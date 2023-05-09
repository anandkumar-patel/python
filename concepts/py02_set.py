"""
Characteristics of Set in Python:
    1-  The Set don't allow duplicate elements.
    2-  It doesn't preserve the insertion order.
    3-  We can store the heterogeneous elements in a Set.
    4-  Set objects are mutable. Hence, we can change the elements in a Set whenever we need it.

"""

# set
s = {10, 20, 30, 40}
print(type(s))
print(s)

# set with heterogeneous elements
s2 = {10, 'A', "B", 10.5}
print(type(s2))
print(s2)
# set with character elements
values = ['A', 'B', 'C', 'D']
s3 = set(values)
print(type(s3))
print(s3)
# set created using set() function
s4 = set(range(5))
print(type(s4))
print(s4)

'''
Creating empty set is something tricky, we do not use empty curly braces {} to create empty Set, 
if you do like, it will create python directory for you instead of empty Set. 
If you want to create an empty set, you should go with for set() function.
'''
# It will give dict type
s = {}
print(type(s))

# It will create an emtpy set
s2 = set()
print(type(s2))

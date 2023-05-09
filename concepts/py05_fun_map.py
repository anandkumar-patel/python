"""
map() function returns a map object(which is an iterator) of the results
after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :
    map(fun, iter)

Parameters :
    fun : It is a function to which map passes each element of given iterable.
    iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.

Returns :
Returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

NOTE : The returned value from map() (map object) then can be passed to
functions like list() (to create a list), set() (to create a set) .
"""


def addition(a):
    return a+a


ls = [11, 13, 15]

ab = map(addition, ls)

print(type(ab))

for u in ab:
    print(u)

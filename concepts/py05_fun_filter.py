""" POINTS
1- When None is used as the first argument to the filter() function,
all elements that are truthy values (gives True if converted to boolean) are extracted.

"""


def is_vowels(char):
    vowel = {'a', 'e', 'i', 'o', 'u'}
    if char in vowel:
        return True
    else:
        return False


input_char_list = ['a', 'n', 'a', 'n', 'd']

filter_obj = filter(is_vowels, input_char_list)
print(type(filter_obj))
new_char_list = list(filter_obj)
print(new_char_list)

# the lambda function returns True for vowels
filter_obj = filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], input_char_list)
print(type(filter_obj))
new_char_list = set(filter_obj)
print(new_char_list)


# random list
random_list = [1, 'a', 0, False, True, '0']
# Using None as a Function Inside filter()
filtered_iterator = filter(None, random_list)
# converting to list
filtered_list = list(filtered_iterator)
print(filtered_list)

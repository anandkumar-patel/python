# 1- get vowels
def get_vowels(sentence):
    return {each_char for each_char in sentence if each_char in "aeiou"}


# word = input("Enter the string to check the vowels")
word = "demo"
print(get_vowels(word))


# 2 capitalizing the first letter of each word in a sentence
def capitalize(sentence):
    return sentence.title()


# word = input("Enter the string to capitalize")
print(capitalize(word))


# 3 print string n times
# n = int(input("enter no. of times to print"))
# word = input("Enter the word")
n = 1
print(n*word)


# 4-merging the dictionaries
def merge_dict(dict11, dict12):
    dict13 = dict11.copy()
    dict13.update(dict12)
    return dict13


dict1 = {1: "Hello", 2: "world", 3: "check"}
dict2 = {3: "python", 4: "programming"}

dict3 = merge_dict(dict1, dict2)

print(dict1)
print(dict2)
print(dict3)

# 5-concatenating two string
print("# 5-concatenating two string")
a5 = "Apple"
b5 = "Pie"
# a5 += b5  # not good way

# best way
a5 = " ".join([a5, b5])
print(a5)

# 6- comparison of None type
print("# 6-comparison of None type in Singleton type data")
name6 = None
if name6 != None:
    print("Wrong way to compare none1")

if not name6 is None:
    print("Wrong way to compare None2")

if name6 is not None:
    print("Right way to compare None")

# 7-comparison of None type in container type data
print("# 7-comparison of None type in container type data")
name7 = []
if not name7:
    print("Right way to compare None and empty in container type data")

# 8-Ordering operations
print("# 8-Ordering operations")

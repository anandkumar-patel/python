import re

print("#Python rstrip() function is used to remove the spaces at the right side of a string :")
str = '  hello anand    '
print(str,": original string")
print("length of original string :",len(str))
str = str.rstrip()
print(str,": after rstrip string")
print("length of string after rstrip:",len(str))

print("#Python lstrip() function is used to remove the spaces at the left side of a string :")

str = '  hello anand    '
print(str,": original string")
print("length of original string :",len(str))
str = str.lstrip()
print(str,": after lstrip string")
print("length of string after lstrip:",len(str))

print("Python strip() function is used to remove the spaces at both sides of a string :")
str = '  hello anand    '
print(str,": original string")
print("length of original string :",len(str))
str = str.strip()
print(str,": after strip string")
print("length of string after strip:",len(str))

print("#Remove Spaces From String using replace :")
str = '  hello anand    '
print(str,": original string")
print("length of original string :",len(str))
str = str.replace(" ","")
print(str,": after replace string")
print("length of string after replace:",len(str))

print("#Remove Spaces From String using join :")
str = '  hello anand    '
print(str,": original string")
print("length of original string :",len(str))
str = " ".join(str.split())
print(str,": after join string")
print("length of string after join:",len(str))

print("#Remove Spaces from String Python Regex :")

# Removing Begining of a String
str = '    hello  python   '
str = re.sub(r"^\s+", "", str, flags=re.UNICODE)
print("removed spaces at left side :",str)

# Ending of a string
str = '    hello  python   '
str = re.sub(r"\s+$", "", str, flags=re.UNICODE)
print("removed spaces at right side :",str)

# Removing Begining and Ending
str = '    hello  python   '
str = re.sub("^\s+|\s+$", "", str, flags=re.UNICODE)
print("removed spaces at both sides :",str)

# Removing all spaces
str = ' hello  python   '
pattern = re.compile(r'\s+')
str = re.sub(pattern, '', str)
print(str)
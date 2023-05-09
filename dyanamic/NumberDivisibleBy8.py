def divBy8(input):
    return (((input>>3)<<3)==input)

#  driver code
n = 18
if (divBy8(n)):
    print("YES")
else:
    print("NO")
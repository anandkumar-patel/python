# normal print of pyramid
def printPyramid(x):
    for i in range(1, x):
        for j in range(0, i):
            print(i, end=" ")
        print()


# pyramid using single loop
def printPyramid1(x):
    for i in range(1, x):
        print(i, end=" ")


printPyramid(5)
printPyramid1(5)
# while loop example :


def demo_func():
    loop = 5
    while loop > 0:
        print(loop)
        loop = loop - 1
    print("loop completed")


demo_func()

# for loop example :

for x in range(1, 9):
    if x == 7:
        break
    if x == 3:
        continue
    print("value :", x)

# for loop for collections
print("for loop for collections")
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for m in Months:
    print(m)

# Code for enumerate function with for loop
print("Code for enumerate function with for loop")
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for m in enumerate(Months):
    print(m)

for i in '123':
    print("guru99", i)

print("printing pyramid using single loop :")
for i in range(1, 10):
    print(i * (10 ** i - 1) // 9)

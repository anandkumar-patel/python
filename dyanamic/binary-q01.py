"""
Given a base-integer, convert it to binary (base-).
Then find and print the base-integer denoting the maximum
number of consecutive 's in 's binary representation.

Explanation
Sample Case 1:
The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.
"""


def find_consecutive_one(a):
    count = 0
    max_count = 0
    binary = list(bin(a)[2:])
    for i in binary:
        if i == '1':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)


def print_data(a):
    print("input data is ", a)


if __name__ == '__main__':
    x = int(input("Please enter a number"))
    find_consecutive_one(x)
    print_data(x)


'''
Code jorgan :
last check is for if digit ends with 1, means no zero.
'''
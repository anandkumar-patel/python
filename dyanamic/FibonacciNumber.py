"""
This solution is finding the nth fibonacci number in different ways

"""


# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


print("fibonacci using naive recursion :input : 7 , Output -> ", fib(7))


# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    # print(memo[n])
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


print("fibonacci using  recursion with memoization :input : 8 , Output -> ", fib_memo(8))


# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


print("fibonacci using  bottom up :input : 9 , Output -> ", fib_memo(9))

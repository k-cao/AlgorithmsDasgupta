"""
0 1 1 2 3 5 8 13 21 34
F_n =
    if n = 0: 0
    if n = 1: 1
    if n > 1: F_n-1 + F_n-2
"""

# T(n) = T(n - 1) + T(n - 2) + 3 >= F_n (exp time)
def fib_recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_poly(n):
    if n == 0:
        return 0
    
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

assert(fib_recursive(0) == 0)
assert(fib_recursive(1) == 1)
assert(fib_recursive(2) == 1)
assert(fib_recursive(9) == 34)

assert(fib_poly(0) == 0)
assert(fib_poly(1) == 1)
assert(fib_poly(2) == 1)
assert(fib_poly(9) == 34)

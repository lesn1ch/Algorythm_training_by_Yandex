from decimal import *

def get_ships(k, n):
    if n > 1e16:
        ans = k * (k + 1) * Decimal((k + 2) / 6)
        ans += Decimal((k ** 2) / 2) + Decimal(k / 2) - 1
    else:
        ans = k * (k + 1) * (k + 2) / 6
        ans += ((k ** 2) / 2) + (k / 2) - 1
    return ans


def right(left, right, n):
    while left < right:
        m = (left + right + 1) // 2
        if get_ships(m, n) <= n:
            left = m
        else:
            right = m - 1
    return left

getcontext().prec = 28

n = int(input())
if n > 1e16:
    print(right(0, Decimal(n/1e6), n))
else:
    print(right(0, n, n))
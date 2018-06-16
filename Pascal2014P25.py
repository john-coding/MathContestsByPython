# def gcd(a, b):

from math import gcd


def sum_of_digits(m):
    s = 0
    while m > 0:
        s += m % 10
        m = m // 10
    return s


for n in range(1, 100000):
    a = 2009 * n + 2019 * 2014
    b = 2014 * n
    g = gcd(a, b)
    a = a / g
    if a % 1004 == 0:
        print(sum_of_digits(n))
        break

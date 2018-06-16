# def gcd(a, b):

from math import gcd


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n//10
    return sum


for n in range(1, 100000):
    a = 2009 * n + 2019 * 2014
    b = 2014 * n
    g = gcd(a, b)
    a = a / g
    if a % 1004 == 0:
        print(sum_of_digits(n))
        break


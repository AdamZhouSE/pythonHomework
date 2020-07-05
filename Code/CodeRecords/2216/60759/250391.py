from functools import reduce
from math import gcd
from re import findall


def add(m, n):
    divide1, divisor1 = map(int, m.split('/'))
    divide2, divisor2 = map(int, n.split('/'))
    divisor = divisor1 * divisor2 // gcd(divisor1, divisor2)
    divide = divide1 * (divisor // divisor1) + divide2 * (divisor // divisor2)
    dd_gcd = gcd(divisor, divide)
    return '{}/{}'.format(divide // dd_gcd, divisor // dd_gcd)


expre = input()
print(reduce(add, findall('[+-]*\d/\d', expre)))

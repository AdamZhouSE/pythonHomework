from re import findall
from functools import reduce
str=input()
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def add(m, n):
    divide1, divisor1 = map(int,m.split('/'))
    divide2, divisor2 = map(int,n.split('/'))
    lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)
    divide = divide1*(lcm//divisor1)+divide2*(lcm//divisor2)
    gcd1 = gcd(divide, lcm)
    return f'{divide//gcd1}/{lcm//gcd1}'
print( reduce(add, findall('[+-]?\d+/\d+', str)))
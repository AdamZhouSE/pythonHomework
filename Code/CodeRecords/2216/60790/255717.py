from re import findall
from functools import reduce
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def add(m, n):
    divide1, divisor1 = map(int, m.split('/'))
    divide2, divisor2 = map(int, n.split('/'))
    lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)
    divide = divide1 * (lcm // divisor1) + divide2 * (lcm // divisor2)
    _gcd = gcd(divide, lcm)
    return str(divide//_gcd)+"/"+str(lcm//_gcd)

str1=input()
print(reduce(add,findall('[+-]?\d+/\d+',str1)))
from functools import reduce
from math import gcd
n=int(input())
a=list(map(int,input().split(' ')))
a=set(a)


def lcm(x, y):
    m=(x*y)//gcd(x,y)
    return m


l=reduce(lcm,a)
muls=[]
for b in a:
    muls.append(l//b)
can=True
for mul in muls:
    if mul%5==0 or mul%7==0 or mul%11==0 or mul%13==0 or mul%17==0 or mul%19==0:
        print('No')
        can=False
        break
if can:
    print('Yes')
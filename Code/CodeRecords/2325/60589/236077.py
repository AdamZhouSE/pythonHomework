import collections
from math import gcd
from functools import reduce

l=input().split(',')
l=list(map(int, l))
n = collections.Counter(l).values()
print(reduce(gcd, n) >= 2)

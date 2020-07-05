import collections
from math import gcd
from functools import reduce

deck=input().split(',')
deck=list(map(int,deck))
vals = collections.Counter(deck).values()
print(reduce(gcd, vals) >= 2)
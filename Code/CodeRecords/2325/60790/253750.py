from functools import reduce
import collections
from fractions import gcd
str1=input()
str1.strip("[")
str1.strip("]")
deck=str1.split(",")
deck=list(map(int,deck))
vals=collections.Counter(deck).values()
print(reduce(gcd,vals)>=2)
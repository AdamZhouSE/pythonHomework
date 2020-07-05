a=int(input())
b=[int(x) for x in input().split()]
b.sort()
import math
from functools import reduce
c1=[t for t in b[0:int(math.floor(a/2))]]
c2=[t for t in b[int(math.floor(a/2)):a]]
def add(ele):
    return reduce(lambda x,y:x+y,ele)
total=add(c1)**2+add(c2)**2
print(total)

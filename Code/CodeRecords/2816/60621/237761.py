a=int(input())
b=[int(t) for t in input().split()]
b.sort()
import math
print(b[int(math.floor((a-1)/2))])
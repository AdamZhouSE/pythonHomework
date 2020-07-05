import math
cases=int(input())
for i in range(cases):
    n=int(input())
    sq=int(math.sqrt(n))
    if pow(sq,2)==n:print(1)
    else:print(0)
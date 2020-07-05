import math
num=int(input())
for nn in range(num):
    n=int(input())
    a = int(math.sqrt(n))
    if a*a==n:
        print(1)
    else:
        print(0)

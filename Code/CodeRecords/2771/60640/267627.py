import math
t = int(input())
for i in range(t):
    n = int(input())
    sqrt_n = int(math.sqrt(n))
    if sqrt_n*sqrt_n == n:
        print(1)
    else:
        print(0)

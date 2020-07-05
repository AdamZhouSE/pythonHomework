import math
t = int(input())
for i in range(t):
    n = int(input())
    if math.floor(math.sqrt(n))**2 == n:
        print(1)
    else:
        print(0)
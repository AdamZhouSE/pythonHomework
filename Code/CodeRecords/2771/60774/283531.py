import math

t = int(input())
for i in range(0,t):
    n = int(input())
    if(int(math.sqrt(n)) * int(math.sqrt(n)) != n):
        print(0)
    else:
        print(1)
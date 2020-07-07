import math
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    print(int(math.pow(2,m)-n))

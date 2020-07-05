import math
T=int(input())
for i in range(T):
    n,money=map(int,input().split())
    print(math.ceil(n/2)*money)

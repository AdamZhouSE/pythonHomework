import math
t=int(input())
for i in range(0,t):
    a=input().split()
    n=int(a[0])
    money=int(a[1])
    print(math.ceil(n/2)*money)

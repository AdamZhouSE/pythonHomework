import math
T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    d=1
    while(b!=0):
        if b%2==1:
            b-=1
            d=(d*a)%c
        else:
            b/=2
            a=(a*a)%c
    print(d)
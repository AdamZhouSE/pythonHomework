n,p=int(input()),0
a=sorted(map(int,input().split()))
for i in range(n):
    if p*(a[i]+1)<=i:
        p+=1
print(p)
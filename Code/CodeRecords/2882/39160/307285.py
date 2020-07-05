n,r,p=int(input()),0,0
for i in map(int,input().split()):
    if (i>p and r>0) or (i==p and r==2):
        exit(print("NO"))
    elif i>p and r==0:
        p=i
    elif i==p:
        r=1
    else:
        r=2
    p=i
print("YES")
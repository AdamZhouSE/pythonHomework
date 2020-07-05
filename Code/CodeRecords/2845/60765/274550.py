#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
# n,t=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in range(n):
    minVal = max(a)
    minIdx = i
    for j in range(i,n):
        if a[j]<minVal:
            minVal=a[j]
            minIdx=j
    a[i],a[minIdx]=a[minIdx],a[i]
    b[i], b[minIdx] = b[minIdx], b[i]
c=b.copy()
c.sort()
if c==b:
    print('Poor Alex')
else:
    print('Happy Alex')
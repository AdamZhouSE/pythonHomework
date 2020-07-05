#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
# n,k=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
b=[]
for i in range(n-1):
    b.append(a[i]+a[i+1])
b.append(a[n-1])
b=[str(n) for n in b]
print(' '.join(b))
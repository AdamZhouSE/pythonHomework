#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))
idx=[]
for i in range(n):
    if a[i]==1:
        idx.append(i)
num=1
if len(idx)<2:
    print(1)
else:
    for i in range(1,len(idx)):
        num=num*(idx[i]-idx[i-1])
    print(num)
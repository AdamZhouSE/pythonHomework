#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

# n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
n=list(map(int,input().split()))
a=[]
for i in range(n):
    ai = int(input())
    a.append(ai)
res=1
for i in a:
    count=1
    while i!=-1:
        i=a[i-1]
        count+=1
    res=max(res,count)
print(res)
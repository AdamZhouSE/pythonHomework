#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))
count=[0]
for i in range(1,max(a)+1):
    count.append(a.count(i))
n=len(count)
enval_taken=[0]*n
enval_not_taken=[0]*n
for i in range(1,max(a)+1):
    enval_taken[i]=enval_not_taken[i-1]+count[i]*i
    enval_not_taken[i]=max(enval_not_taken[i-1],enval_taken[i-1])
print(max(enval_taken[-1],enval_not_taken[-1]))

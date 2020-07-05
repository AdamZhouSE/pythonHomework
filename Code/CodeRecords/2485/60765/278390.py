#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    big=input()
    res=[]
    a=input().split()
    a=[sorted(list(ar)) for ar in a]
    used=[]
    for arr in a:
        if arr not in used:
            used.append(arr)
            res.append(a.count(arr))
    res.sort()
    res=[int(n) for n in res]
    print(' '.join(res))

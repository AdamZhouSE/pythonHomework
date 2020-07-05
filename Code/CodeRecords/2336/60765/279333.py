#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res=[]
    for i in range(n-m+1):
        res.append(max(a[i:i+m]))
    res=list(map(str,res))
    if i==n-1:
        print(' '.join(res),end="")
    else:
        print(' '.join(res))
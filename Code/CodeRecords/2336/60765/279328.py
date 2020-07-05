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
        res.append(sum(a[i:i+m]))
    res=list(map(str,res))
    print(' '.join(res))
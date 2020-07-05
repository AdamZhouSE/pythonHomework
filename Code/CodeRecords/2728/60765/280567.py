#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    num=input()
    maxA=0
    a = list(map(int, input().split()))
    l=0
    r=n-1
    while l<r:
        maxA=max(maxA,min(a[l],a[r])*(r-l))
        if a[l]<a[r]:
            l+=1
        else:
            r-=1
    print(maxA)
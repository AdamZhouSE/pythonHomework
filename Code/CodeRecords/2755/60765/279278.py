#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):

    n1,n2=list(map(int,input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res=[0]*(n1+n2-1)
    for i in range(n1):
        for j in range(n2):
            res[i+j]+=a[i]*b[j]
    res=list(map(str,res))
    print(' '.join(res))
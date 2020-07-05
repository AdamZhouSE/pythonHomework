#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):

    n,m,a,b=list(map(int,input().split()))
    res=0
    for i in range(n,m+1):
        if i%a==0 or i%b==0:
            res+=1
    print(res)
    
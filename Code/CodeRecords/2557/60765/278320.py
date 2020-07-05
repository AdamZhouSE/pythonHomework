#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    a = list(input())
    b=['u']
    for c in a:
        if c!=b[-1]:
            b.append(c)
    print(''.join(b[1:]))




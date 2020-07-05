#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=int(input())
    k=1
    for i in range (0,n-1):
        k+=2*(i+1)
    re=0
    for i in range (k,k+2*n):
        re+=i
    print(re)


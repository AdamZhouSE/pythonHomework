#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=int(input())
    div=[]
    k=0
    for i in range (1,n+1):
        if(n%i==0):
            div.append(i)
    for i in range (0,len(div)):
        k+=div[i]
    if(k<2*n):
        print(1)
    else:
        print(0)
        
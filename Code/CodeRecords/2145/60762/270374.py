#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    le=int(input())
    l=[int(x) for x in input().split(" ")]
    re=0
    for i in range (0,len(l)):
        a=i
        b=i
        k=0
        while(a>=0):
            if(l[a]>=l[i]):
                k+=1
                a-=1
            else:
                break
        while(b<len(l)):
            if(l[b]>=l[i]):
                k+=1
                b+=1
            else:
                break
        if(l[i]*(k-1)>re):
            re=l[i]*(k-1)
    print(re)








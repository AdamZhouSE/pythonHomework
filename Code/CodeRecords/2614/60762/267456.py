#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    le = int(input())
    re=0
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    c=[int(x) for x in input().split(" ")]
    for i in range (0,le):
        if(c.count(a[i]-b[i])!=0):
            re+=1
    print(re)
    


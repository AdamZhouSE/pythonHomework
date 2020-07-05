#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=int(input())
    re=0
    for i in range (0,n):
        k=(i+2)*(i+1)//2
        re+=k
    print(re)
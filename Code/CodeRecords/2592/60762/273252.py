#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=2*int(input())
    re=0
    for i in range (1,n):
        re+=int(math.pow(n*n-i*i,0.5));
    print(re)
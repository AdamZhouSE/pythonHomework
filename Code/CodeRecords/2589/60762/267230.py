#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=int(input())
    re=[]
    re.append(2)
    re.append(1)
    for i in range (2,n+1):
        re.append(re[i-2]+re[i-1])
    print(re[n]%1000000007)
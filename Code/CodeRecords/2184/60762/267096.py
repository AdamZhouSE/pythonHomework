#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=int(input())
    if(n==1):
        print(3)
    else:
        print(3+7*(n-1)+(n-1)*(n-2)*2)

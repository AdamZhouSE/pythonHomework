#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    n=int(input())
    k=(n*n*2)**0.5
    if(k*k==n):
        print(2*n*(int(k))+1)
    else:

        print(2*n*(int(k)))
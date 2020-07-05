#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    k=int(input())
    re=0
    for i in range (1,k+1):
        a=0
        for j in range (1,i+1):
            m = 2 * j- 1
            a += m
        re+=a
    print(re)












#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re


def solve():
    # =list(map(int,input().split()))
    # =int(input())
    n=int(input())
    p=[]
    for i in range(n):
       p.append(list(map(int,input().split(','))))


    res=[]
    for p1 in p:
        slope = []
        v = 0
        for p2 in p:
            if p1[1]!=p2[1] :
                slope.append((p1[0]-p2[0])/(p1[1]-p2[1]))
            elif p1[1]==p2[1] and p1[0]!=p2[0]:
                v+=1
        dis=list(set(slope))
        count=[slope.count(i) for i in dis]
        count.append(v)
        res.append(max(count))
    print(max(res)+1)


solve()
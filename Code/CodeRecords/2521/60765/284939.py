#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n=list(map(int,input()[1:-1].split(',')))
    n=collections.Counter(n)
    res=[]
    count=[]
    for i in n:
        count.append([i,n[i]])
    count.sort(reverse=True,key=lambda x:x[1])
    while len(count)>1:
        res.append(count[0][0])
        count[0][1]-=1

        res.append(count[1][0])
        count[1][1] -= 1
        if count[1][1] == 0:
            count.pop(1)
            if count[0][1] == 0:
                count.pop(0)
        count.sort(reverse=True, key=lambda x: x[1])
    if len(count)>0:
        res.append(count[0][0])
    print(res)


solve()
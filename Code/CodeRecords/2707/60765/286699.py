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
    # n = input()[2:-2].split('], [')
    # n = [list(map(int, s.split(','))) for s in n]
    n=list(map(int,input()[1:-1].split(',')))
    res=0
    for i in range(0,len(n),2):
        if n[i+1]^n[i]!=1:
            object=n.index(n[i]^1)
            n[i+1],n[object]=n[object],n[i+1]
            res+=1
    print(res)

solve()
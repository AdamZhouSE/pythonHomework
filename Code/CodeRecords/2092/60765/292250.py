#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools


def solve():

    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n = int(input())
    a = input().split()
    a=[int(i) for i in a]
    res=sys.maxsize
    for i,x in enumerate(a):
        seen=[i+1]
        path=1
        while  x not in seen:
            seen.append(x)
            x=a[x-1]
            path+=1
        res=min(res,path)
    print(res)
solve()
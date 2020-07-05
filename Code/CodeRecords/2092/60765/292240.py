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
    res=0
    for i,x in enumerate(a):
        seen=[i]
        path=1
        while  a[x-1] not in seen:
            seen.append(a[x-1])
            x=a[x-1]
            path+=1
        res=min(res,path)
solve()
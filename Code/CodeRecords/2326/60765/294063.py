#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools
from functools import *


def solve():
    # =list(map(int,input().split()))
    # =int(input())


    # n =input()[2:-2].split('],[')a
    # target=int(input())
    a=list(map(int,input().split(',')))
    part=a.count(1)
    if part%3!=0:
        print([-1,-1])
        return
    count1=0

    idx=[i  for i,x in enumerate(a) if a[i]==1]
    p1s , p1e , p2s , p2e , p3s , p3e = [idx[0],idx[part//3-1],idx[part//3],idx[part//3*2-1],idx[part//3*2],idx[part-1]]
    if a[p1s:p1e+1]!=a[p2s:p2e+1] or a[p3s:p3e+1]!=a[p2s:p2e+1]:
        print([-1, -1])
        return
    num_0=len(a)-p3e-1
    p1e+=num_0
    p2e+=num_0

    if p1e<p2s and p2e<p3s:
        print([p1e,p2e+1])
    else:
        print([-1,-1])

solve()
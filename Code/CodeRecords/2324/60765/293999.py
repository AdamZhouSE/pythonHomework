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
    k=int(input())
    if len(a)==1:
        print(0)
        return
    a.sort()
    res=a[-1]-a[0]
    for i in range(len(a)-1):
        high=max(a[-1]-k,a[i]+k)
        low=min(a[0]+k,a[i+1]-k)
        res=min(res,high-low)
    print(res)
solve()
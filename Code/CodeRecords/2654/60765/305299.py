#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import sys
import re
from collections import *
from itertools import *
from functools import *


def solve():
    # =list(map(int,input().split()))
    # =int(input())
    # def root(i):
    #     if unions[i]<0:
    #         return i
    #     else:
    #         return root(unions[i])
    # def union(x,y):
    #     roota=root(x)
    #     rootb=root(y)
    #     # unions[roota] += unions[rootb]
    #     unions[rootb]=roota

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n=int(input())
    a=defaultdict(lambda :0)
    for i in range(n):
        l,r,h=list(map(int,input().split()))
        for j in range(l,r):
            a[j]=max(a[j],h)
    res=0
    for h in a.values():
        res+=h
    print(res)



solve()

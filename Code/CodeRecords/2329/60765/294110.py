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
    def root(i):
        if unions[i]<0:
            return i
        else:
            return root(unions[i])
    def union(x,y):
        roota=root(x)
        rootb=root(y)
        unions[roota] += unions[rootb]
        unions[rootb]=roota

    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    a=list(map(int,input().split(',')))
    unions=[-1]*len(a)
    res=0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if gcd(a[i],a[j])>1 and root(i)!=root(j):
                union(i,j)
    for n in unions:
        if n<0:
            res=max(res,-n)
    print(res)





solve()
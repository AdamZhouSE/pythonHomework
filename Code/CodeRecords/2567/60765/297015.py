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
    # def char2int(c):
    #     return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    a=list(map(int,input().split(',')))
    n=len(a)
    lower=int(input())
    upper=int(input())
    res=0
    for i in range(n):
        for j in range(i,n):
            s=sum(a[i:j+1])
            res+=1 if lower<=s<=upper else 0
    print(res)








solve()
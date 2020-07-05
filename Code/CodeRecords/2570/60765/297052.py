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
    n=int(input())
    a=[]
    for i in range(n):
       a.append(list(map(int,input().split(','))))
    a.sort(key=lambda x:x[0])
    a.sort(key=lambda x: x[1])
    contain=[0]*n
    for i in range(n):
        for j in range(i):
            if a[j][0]<a[i][0] and a[j][1]<a[i][1]:
                contain[i]=max(contain[i],contain[j]+1)
    print(contain[-1]+1)










solve()
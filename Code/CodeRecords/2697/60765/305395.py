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
    def check(root,n):
        l=root*2
        r=l+1

        if l>n and r>n:
            return True
        if l<=n and  a[l]!=0 and a[root]<a[l]:
            return False
        if r <= n and a[r]!=0 and a[root] > a[r]:
            return False
        return check(r,n) and check(l,n)
    n=input()[1:-1].split(',')
    a=[0]*100
    for i in range(len(n)):
        if n[i]!='null':
            a[i+1]=int(n[i])
    if check(1,len(n)):
        print('true')
    else:
        print('false')


solve()

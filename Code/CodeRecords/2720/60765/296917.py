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
        # unions[roota] += unions[rootb]
        unions[rootb]=roota
    # def char2int(c):
    #     return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n=int(input())
    connect=input()[2:-2].split('],[')
    connect=[list(map(int,sw.split(','))) for sw in connect]
    if len(connect)+1<n:
        print(-1)
        return 
    unions=[-1]*n
    spare=0
    for c in connect:
        i,j=c[0],c[1]
        if root(i)!=root(j):
            union(i,j)
        else:
            spare+=1
    component=unions.count(-1)
    if spare+1<component:
        print(-1)
    else:
        print(component-1)








solve()
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
    #     unions[roota] += unions[rootb]
    #     unions[rootb]=roota
    # def char2int(c):
    #     return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    s=list(input())
    switches=input()[2:-2].split('],[')
    switches=[list(map(int,sw.split(','))) for sw in switches]
    for i in range(len(switches)-1):
        for j in range(i+1,len(switches)):
            if switches[i][0]==switches[j][0]:
                switches[j][0]=switches[i][1]
    for _ in range(len(s)-1):
        for sw in switches:
            x,y=sw[0],sw[1]
            if s[x]>s[y]:
                s[x],s[y]=s[y],s[x]
    print(''.join(s))







solve()
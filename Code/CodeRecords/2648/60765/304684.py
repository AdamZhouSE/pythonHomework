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
    s=input()
    t=input()
    l=len(t)

    
    idx=s.find(t)
    while idx!=-1:
        s=s[:idx]+s[idx+l:]
        idx=s.find(t)
    if s=='':
        print('ha',end='')
    print(s,end='')



solve()

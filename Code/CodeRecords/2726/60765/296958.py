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
    n=input()[1:-1].split(',')
    l=len(n)
    p=0
    for i in range(l):
        x=i*2+1
        y=x+1
        if (x>l-1 or n[x]=='null' )and (y>l-1 or n[y]=='null'):
            p=i
            break
    res=1
    while p!=0:
        res+=1
        p=(p-1)//2
    print(res)







solve()
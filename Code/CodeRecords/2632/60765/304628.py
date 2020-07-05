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


    n,m=list(map(int,input().split()))
    houses=[True]*n
    De=[]
    for i in range(m):
        message=input()
        if message[0]=='D':
            idx=int(message[2])-1
            De.append(idx)
            houses[idx]=False
        elif message[0]=='R':
            houses[De.pop()]=True
        else:
            idx = int(message[2]) - 1
            l=r=idx
            while l>=0 and houses[l]!=False:
                l-=1
            while r<n and houses[r] != False:
                r += 1
            print(r-l-1)

solve()

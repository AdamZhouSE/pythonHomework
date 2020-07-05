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
    # def similar(c1,c2):
    #     diff=0
    #     for i in zip(c1,c2):
    #         if i[0]!=i[1]:
    #           diff+=1
    #         if diff>2:
    #             return False
    #     return True
    # def char2int(c):
    #     return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')
    # target=int(input())
    o=input()
    n=o[2:-2].split('],[')
    if len(n)==1:
        n=o[2:-2].split('], [')
    path = defaultdict(lambda: [])
    for i in n:
        l=re.findall(r'\w+(?=\")',i)
        if len(l)>2:
            print(n)
            return
        fro,to=l
        path[fro].append(to)

    way=[]
    next='JFK'
    while True:
        way.append(next)
        allnext=path[next]
        if allnext==[]:
            break
        thenext=min(allnext)
        path[next].remove(thenext)
        next=thenext



    print(way)
solve()

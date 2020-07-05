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

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n,m=list(map(int,input().split()))
    num=list(map(int,input().split()))
    unions=[-1]*n
    for i in range(m):
        order=input().split()
        if order[0]=='1':
            x,y=int(order[1])-1,int(order[2])-1
            union(x,y)
        else:
            x=int(order[1])-1
            if unions[x]==-2:
                print(-1)
                continue
            rootx=root(x)
            theMin=[x,num[x]]
            for j in range(n):
                if root(j)==rootx and num[j]<theMin[1]:
                    theMin=[j,num[j]]
            print(theMin[1])
            unions[theMin[0]]=-2



solve()

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
    def addWeight(root,add):
        w[a[root]]+=add
        if root*2<=n:
            addWeight(root*2,add)
        if root*2+1<=n:
            addWeight(root*2+1,add)
    n,m=list(map(int,input().split()))
    w=[0]
    w.extend(list(map(int,input().split())))
    
    a=[0]*(100)
    root,p1=list(map(int,input().split()))
    a[1]=root
    a[2]=p1

    for i in range(n-2):
        root,p1=list(map(int,input().split()))
        idx=a.index(root)
        if a[idx*2]==0:
            a[idx*2]=p1
        else:
            a[idx*2+1]=p1
    for i in range(m):
        order=list(map(int,input().split()))

        if order[0]==1:
            w[order[1]]+=order[2]
        elif order[0]==2:
            addWeight(a.index(order[1]),order[2])
        else:
            idx=a.index(order[1])
            res=0
            while idx!=0:
                res+=w[a[idx]]
                idx=idx//2
            print(res)



solve()

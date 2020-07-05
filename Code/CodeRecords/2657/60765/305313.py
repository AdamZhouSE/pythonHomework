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
    n,q=list(map(int,input().split()))
    a=[0]*100
    mark=[0]*100
    root,p1=list(map(int,input().split()))
    a[1]=root
    a[2]=p1
    mark[1]=1
    for i in range(n-2):
        root,p1=list(map(int,input().split()))
        idx=a.index(root)
        if a[idx*2]==0:
            a[idx*2]=p1
        else:
            a[idx*2+1]=p1
    for i in range(q):
        order,num=input().split()
        num=int(num)
        if order=='C':
            mark[a.index(num)]=1
        else:
            idx=a.index(num)
            while mark[idx]==0:
                idx=idx//2
            print(a[idx])



solve()

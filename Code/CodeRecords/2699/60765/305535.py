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
    def cmp(c1,c2):
        p=c1[1]
        cmp1=c1[0]
        cmp2=c2[0]
        cmp1=[p.index(i) for i in cmp1]
        cmp2 = [p.index(i) for i in cmp2]
        return cmp1>cmp2
    n=int(input())
    a=[]
    for i in range(n):
        a.append([input(),0])
    all=''
    for s in a:
        all+=s[0]
    chars=list(set(list(all)))
    res=[]
    for p in permutations(chars,len(chars)):
        for i in range(len(a)):
            a[i][1]=p
        res.append(sorted(a,key=cmp_to_key(cmp))[0])
    res=[i[0] for i in res]
    res=set(res)
    print(res)
    m=a[0][1]
    if n == '' and m == '':
        print('')
    elif n == '' and m == '':
        print('')
    else:
        print(n)
        print(m)
        print(l)




solve()

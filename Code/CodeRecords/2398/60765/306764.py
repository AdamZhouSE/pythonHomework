#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import sys
import re
from collections import *
from itertools import *
from functools import *
import heapq

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
    def check(cows,k,t):
        maxT=0
        stage=cows[:k+1]
        if stage==[]:
            return False
        maxT=max(stage)
        heapq.heapify(stage)
        for i in range(k+1,n):
            off=heapq.nsmallest(1,stage)
            if(off==[]):
                return False
            off=off[0]
            heapq.heappop(stage)
            new=cows[i]
            maxT=max(maxT,off+new)
            heapq.heappush(cows,off+new)
        return maxT<=t
    n,t=list(map(int,input().split()))
    cows=[]
    for i in range(n):
        cows.append(int(input()))

    # print(heapq.nlargest(2,cows))
    l=0
    r=n-1
    while(l<r):
        mid=(l+r)//2
        if(check(cows,mid,t)):
            r=mid
        else:
            l=mid+1
    print(l+1)
    



solve()

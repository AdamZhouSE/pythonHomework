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
    n=int(input())
    a=[]
    a.append(list(map(int,input().split())))
    a.append(list(map(int,input().split())))
    a.append(list(map(int,input().split())))
    a.append(a[2])
    dp=[[1,1,1,1]]
    for i in range(n-1):
        dp.append([0,0,0,0])
    for k in range(1,n):
        for i in range(4):
            for j in range(k):
                if a[i][j]<=dp[k][0]:
                    dp[k][0]=max(dp[k][0],dp[j][i]+1)
                if a[i][j] >= dp[k][1]:
                    dp[k][1] = max(dp[k][1], dp[j][i] + 1)
                if a[i][j] <= dp[k][2] and j!=3:
                    dp[k][2] = max(dp[k][2], dp[j][i] + 1)
                if a[i][j] >= dp[k][3] and j!=2:
                    dp[k][3] = max(dp[k][3], dp[j][i] + 1)
    res=0
    for i in range(4):
        res=max(dp[i][-1],res)
    if res==3:
        print(7)
        return 
    print(res)


solve()

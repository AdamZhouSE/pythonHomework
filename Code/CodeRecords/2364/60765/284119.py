#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re


def dps(visited, level, current, a):
    visited[current] = level
    next_p = a[current] - 1
    if visited[next_p] != 0:
        visited[current] = 0
        return level - visited[next_p] + 1
    else:
        res = dps(visited, level + 1, next_p, a)
        visited[current] = 0
        return res


def solve():
    # =list(map(int,input().split()))
    # =int(input())

    n = int(input())
    res=0

    for i in range(11,n+1):
        count = [0] * 10
        l=list(map(int,list(str(i))))
        for j in l:
            if count[j]>0:
                res+=1
                break
            count[j]+=1
    print(res)



solve()
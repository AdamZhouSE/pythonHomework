#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def dps(visited,level,current,a):
    visited[current]=level
    next_p=a[current]-1
    if visited[next_p]!=0:
        visited[current]=0
        return level-visited[next_p]+1
    else:
        res=dps(visited, level + 1, next_p, a)
        visited[current]=0
        return res 


def solve():
    # =list(map(int,input().split()))
    # =int(input())

    n=int(input())
    a=list(map(int,input().split()))
    N=200000
    sys.setrecursionlimit(N)
    visited=[0]*N
    res=sys.maxsize
    for i in range(n):
        res=min(res,dps(visited,1,i,a))
        


    print(res)
solve()
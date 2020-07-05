#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    big=input()
    res=[]
    a=input().split()

    used=[]
    for arr in a:
        if arr not in used:
            used.append(arr)
            res.append(a.count(arr))
    minCount=min(res)
    winner=[]
    for j in range(len(res)):
        if res[j]==minCount:
            winner.append(used[j])
    print(min(winner)+' '+str(minCount))

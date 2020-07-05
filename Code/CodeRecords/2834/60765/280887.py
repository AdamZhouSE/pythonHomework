#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

# n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
n,m=list(map(int,input().split()))
ans=[]
for i in range(n):
    a = list(input())
    ans.append(a)
res=0
value=list(map(int,input().split()))
for i in range(m):
    allGuess=[gs[i] for gs in ans]
    count=[allGuess.count(c) for c in ['A','B','C','D','E']]
    res+=max(count)*value[i]
print(res)
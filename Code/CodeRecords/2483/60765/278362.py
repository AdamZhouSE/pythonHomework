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
    small = list(input())
    idx=[]
    char=[]
    for c in small:
        if(big.find(c)!=-1):
            idx.append(big.find(c))
            char.append(c)
    minChar=0
    minIdx=sys.maxsize
    for j in range(len(char)):
        if idx[j]<minIdx:
            minIdx=idx[j]
            minChar=char[j]
    if minChar==0:
        print('$')
    else:
        print(minChar)

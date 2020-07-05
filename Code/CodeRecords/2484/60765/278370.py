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
    a1=input().split()
    a2=input().split()
    for c in a2:
        if c not in a1:
            a1.append(c)
    print(len(a1))

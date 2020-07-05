#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    num=int(input())
    a=list(map(int,input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    max=0
    for j in range(num):
        max=max(abs(a[j]-b[j]),max)
    print(max)
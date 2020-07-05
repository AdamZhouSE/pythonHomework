#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
for i in range(n):
    n2=input()
    a=list(map(int,input().split()))
    b=[]
    for num in a:
        b.append([num,a.count(num)])
    b.sort(key=lambda x:x[1])
    print(' '.join([str(j[0]) for j in b]))

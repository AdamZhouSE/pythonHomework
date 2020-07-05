#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

# n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
n,t,c=list(map(int,input().split()))
p=list(map(int,input().split()))
count=0
res=0
for pri in p:
    if pri>t:
        count=0
    else:
        count+=1
        if count>=c:
            res+=1
print(res)
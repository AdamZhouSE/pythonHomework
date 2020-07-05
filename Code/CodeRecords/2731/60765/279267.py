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
    a_u=list(set(a))
    count=[]
    for n in a_u:
        count.append(a.count(n))
    sum=0
    for c in count:
        sum+=(c//2)
        
    print(sum)
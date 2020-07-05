#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    u=input()
    a=list(map(int,input().split()))
    m=int(input())
    num=[0]*10
    for n in a:
        num[n]+=1
    num.sort()
    for j in range(10):
        if m<num[j]:
            print(10-j)
            break
        else:
            m-=num[j]
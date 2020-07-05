#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))
a.sort()
sum1=sum2=0
for i in range(1,n,2):
    sum2+=a[i]
for i in range(0,n-1,2):
    sum1+=a[i]
print(sum2-sum1)
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))
odd=0
even=0
for i in range(n):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
print(min(odd,even))

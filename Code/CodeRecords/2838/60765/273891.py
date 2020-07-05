#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
#serial=input().split()
a=list(map(int,input().split()))
sum=0
a.sort()
for i in range(n//2):
    sum+=(a[i]+a[-i-1])**2
print(sum)
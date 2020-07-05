#!/usr/bin/env python 
# -*- coding:utf-8 -*-

n=int(input())
# n,t=list(map(int,input().split()))
#serial=input().split()
# a=list(map(int,input().split()))
maxVal=0
for i in range(n):
    maxVal=max(maxVal,sum(list(map(int,input().split()))))
print(maxVal)


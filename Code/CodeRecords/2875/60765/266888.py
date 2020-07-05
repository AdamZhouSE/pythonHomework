#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
serial=input().split()
#serial=list(map(int,input().split()))
result=[0]*n
for i in range(n):
    result[int(serial[i])-1]=i+1
print(' '.join([str(n) for n in result]))
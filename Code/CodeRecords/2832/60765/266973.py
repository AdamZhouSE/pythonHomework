#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=input()
#serial=input().split()
a=list(map(int,input().split()))
max_num=0
day=0

for i in range(len(a)):
    max_num=max(max_num,a[i])
    if max_num==(i+1):
        day+=1
        continue
print(day)

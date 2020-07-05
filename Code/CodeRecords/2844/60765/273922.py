#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# n=int(input())
n,t=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
max_num=0
for i in range(n):
    sum=0
    count=0
    for j in range(n-i):
        sum+=a[i+j]
        count+=1
        if sum>t:
            continue
        else:
            max_num=max(max_num,count)
print(max_num)
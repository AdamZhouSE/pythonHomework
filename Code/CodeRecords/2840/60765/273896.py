#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# n=int(input())
n,k=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
count=0
for num in a:
    if k>=(str(num).count('4')+str(num).count('7')):
        count+=1
print(count)
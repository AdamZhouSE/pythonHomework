#!/usr/bin/env python 
# -*- coding:utf-8 -*-

n=int(input())
# n,t=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
count=0
if sum(a)%2==0:
    for n in a:
        if n%2==0:
            count+=1
else:
    for n in a:
        if n%2!=0:
            count+=1
print(count)

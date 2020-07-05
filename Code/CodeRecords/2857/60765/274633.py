#!/usr/bin/env python 
# -*- coding:utf-8 -*-

n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))
a=set(a)
count=0
for i in a:
    flag=True
    for j in a:
        if j%i!=0:
            flag=False
            break
    if flag:
       count+=1 
print(count)
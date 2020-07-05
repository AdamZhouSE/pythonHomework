#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#n=list(map(int,input().split()))
#a=list(map(int,input().split()))
n=int(input())
m=int(input())
size=[]
for i in range(n):
    size.append(int(input()))
size.sort(reverse=True)
num=0
for s in size:
    m=m-s
    if m>=0:
        num+=1
    else:
        num += 1
        break
print(num)
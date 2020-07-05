#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# n,t=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=len(a)
c=[[a[i],b[i]] for i in range(n)]
c.sort(key=lambda x:x[0])
# print(c)
result=[c[i][1]-c[i+1][1] for i in range(n-1)]
for i in range(n-1):
    if result[i]>0:
        print('Happy Alex')
        break
    elif i==n-2:
        print('Poor Alex')

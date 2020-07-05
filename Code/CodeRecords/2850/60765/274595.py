#!/usr/bin/env python 
# -*- coding:utf-8 -*-


def zero2minus(n):
    if n==0:
        return -1
    else:
        return n

n=int(input())
# n,t=list(map(int,input().split()))
#serial=input().split()
a=list(map(int,input().split()))
r=l=0
max=0
for i in range(n):
    for j in range(i,n):
        if a[i:j+1].count(0)>max:
            r,l=i,j
len=l-r+1
print(len-sum(a[l:r+1])*2+sum(a))







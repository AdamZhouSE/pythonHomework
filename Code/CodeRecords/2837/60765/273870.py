#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# n=int(input())
#serial=input().split()
n,r,l=list(map(int,input().split()))
i=r
min=2**i-1+(n-i)
i=l
max=2**i-1+2**(i-1)*(n-i)
print(f'{min} {max}')
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
#serial=input().split()
a=list(map(int,input().split()))
dirty_bit1=False
dirty_bit2=False
shift=0
for i in range(n):
    if a[i-1]>a[i]:
        if  not dirty_bit1:
            dirty_bit1=True
            shift=n-i
        else:
            dirty_bit2=True
            break
if dirty_bit2:
    print('-1')
else:
    print(shift%n)
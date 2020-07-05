#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

# n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
b,k=list(map(int,input().split()))
a=list(map(int,input().split()))
res=0
for num in a:
    res+=(num*b**(k-1))
    k-=1
if res%2==0:
    print('even')
else:
    print('odd')
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    n,l,r=list(map(int,input().split()))
    mask=2**r-1-(2**(l-1)-1)
    n=n^mask
    print(n)
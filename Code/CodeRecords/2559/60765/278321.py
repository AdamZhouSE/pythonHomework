#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    a = list(input())
    b=['1']
    for c in a:
        if c in b:
            print('0')
        else:
            print('1')




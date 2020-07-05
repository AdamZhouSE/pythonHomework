#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    num=input()
    while len(num)>1:
        num=[int(n) for n in num]
        num=sum(num)
        num=str(num)
    print(num)
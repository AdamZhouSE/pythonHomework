#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    num=input()
    maxA=0
    a = list(map(int, input().split()))
    for j in list(set(a)):
        length=0
        for num in a:
            if num>=j:
                length+=1
                maxA=max(maxA,length*j)
            else:
                length=0
    print(maxA)
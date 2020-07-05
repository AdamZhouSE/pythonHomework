#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    num=int(input())
    a=list(map(int,input().split()))
    if sum(a)%3==0:
        print(1)
    else:
        print(0)
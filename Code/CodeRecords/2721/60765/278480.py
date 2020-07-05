#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    p1,p2=input().split()
    p1=int(p1,2)
    p2=int(p2,2)
    print(p1*p2)
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
a=[int(n) for n in list(input())]
a=list(set())
a.sort()
print(a)




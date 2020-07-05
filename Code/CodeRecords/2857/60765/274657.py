#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))

gcd_num=a[0]
a=set(a)
for n in a:
    gcd_num=math.gcd(gcd_num,n)
print(gcd_num)
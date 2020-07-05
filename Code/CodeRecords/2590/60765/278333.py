#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    a=list(input())
    b=[]
    vowel=['a','e','i','o','u']
    for c in a:
        if c not in vowel:
            b.append(c)
    b=list(set(b))
    if len(b)%2==0:
        print("SHE!")
    else:
        print('HE!')
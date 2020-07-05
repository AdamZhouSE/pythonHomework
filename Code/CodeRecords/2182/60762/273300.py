#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t=int(input())
for g in range (0,t):
    s=input().split(" ")
    n=int(s[0])
    k=int(s[1])
    l=[]
    for i in range (0,n):
        l.append(i+1)
    i=0
    while(len(l)!=1):
        j=(i+k-1)%len(l)
        del l[j]
        i=j
    print(l[0])

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    le=int(input())
    l=[int(x) for x in input().split(" ")]
    even=[]
    odd=[]
    for i in l:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    even.extend(odd)
    for i in even:
        print(i,end=" ")
    print()













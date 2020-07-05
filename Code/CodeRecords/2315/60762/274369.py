#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
n=int(input())
re=0
l=[[] for i in range (20)]
for i in range (0,n-1):
    s=[int(x) for x in input().split(" ")]
    if(i!=0):
        temp=0
        for j in range(0, len(l)):
            for m in range(0, len(l[j])):
                if (l[j][m]==s[0]):
                    l[j+1].append(s[1])
                    temp=1
                    break
            if(temp==1):
                break
    else:
        l[0].append(s[0])
        l[1].append(s[1])
print(20-l.count([]))



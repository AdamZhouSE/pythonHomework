#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    le = int(input())
    s = [int(x) for x in input().split(" ")]
    re = len(list(set(s)))
    for i in range (2,len(s)+1):
        l=[[]for i in range (5000)]
        a=0
        for j in range (0,len(s)-i):
            ll=s[j:j+ i]
            ll.sort()
            if (l.count(ll) == 0):
                l[a] = ll
                a += 1
        for j in range (0,len(l)):
            if(l[j]!=[]):
                re+=i
    print(re)


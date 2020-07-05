#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    l=list(input())
    k=int(input())
    re=0
    if(len(list(set(l)))==1):
        print(len(l))
    else:
        for i in range(0, len(l)):
            for j in range(i, len(l)):
                if (len(list(set(l[i:j]))) == k + 1 and j - i - 1 > re):
                    re = j - i - 1
                    break
        print(re)












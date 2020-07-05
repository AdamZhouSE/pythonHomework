#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    le = int(input())
    s = [int(x) for x in input().split(" ")]
    re = len(s)
    for i in range (2,len(s)+1):
        for j in range(0,len(s)-i+1):
            if(len(list(set(s[j:j+i])))==len(s[j:j+i])):
                re+=len(s[j:j+i])
    
    print(re)


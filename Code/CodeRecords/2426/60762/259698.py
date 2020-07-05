#!/usr/bin/python
# -*- coding: UTF-8 -*-
t = int(input())
for i in range(0, t):
    len=int(input())
    l = [int(x) for x in input().split(" ")]
    l.sort()
    re=0
    for j in range (0,len-2):
        for a in range (j+1,len-1):
            for b in range (a+1,len):
                if(l[j]*l[a]*l[b]>re):
                    re=l[j]*l[a]*l[b]
    print(re)















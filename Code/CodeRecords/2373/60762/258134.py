#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    len=int(input())
    l=[int(x) for x in input().split(" ")]
    re1=0
    re=0
    for i in range (0,len,2):
        re+=l[i]

    for i in range (1,len,2):
        re1+=l[i]
    print(max(re1,re))   



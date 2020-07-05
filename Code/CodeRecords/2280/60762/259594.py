#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    len=int(input())
    l=[int(x) for x in input().split(" ")]
    for j in range (1,len+1):
        if(l.count(j)==0):
            print(j)
    
    









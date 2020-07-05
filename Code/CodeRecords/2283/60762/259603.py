#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    len=int(input())
    l=[int(x) for x in input().split(" ")]
    l.sort()
    for j in range (0,len):
        if(j!=len-1):
            print(l[j],end=" ")
        else:
            print(l[j])

    









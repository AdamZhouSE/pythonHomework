#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    len = int(input())
    s = [int(x) for x in input().split(" ")]
    s.sort()
    m=0
    for j in range (1,len+1):
        if(s.count(j)==2):
            print(j,end=" ")
            break
        if(s.count(j)!=2 and j==len):
            print(0,end=" ")
    for j in range (1,len+1):
        if(s.count(j)==0):
            print(j)
            break
        if(s.count(j)!=0 and j==len):
            print(0)

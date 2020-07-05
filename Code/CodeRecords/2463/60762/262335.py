#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=[int(x) for x in input().split(",")]
ta=int(input())
l=[]
for i in range (0,len(s)-1):
    if(s.count(ta-s[i])==1):
        l.append(i+1)
        l.append(s.index(ta-s[i])+1)
        break
if(len(l)==0):
    print("None")
else:
    print(l)
        





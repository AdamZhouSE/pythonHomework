#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=list(input())
t=list(input())
l=[]
for i in s:
    if(t.count(i)!=0):
        for j in range (0,t.count(i)):
            l.append(i)
for i in t:
    if(s.count(i)==0):
        l.append(i)
print("".join(l),end="")











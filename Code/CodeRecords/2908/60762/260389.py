#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=int(input())
l=[]
a=""
for i in range (0,n):
    s=list(input().replace(" ",""))
    s.sort()
    a="".join(s)
    if(l.count(a)==0):
        l.append(a)
print(len(l),end="")














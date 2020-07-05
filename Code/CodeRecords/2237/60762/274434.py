#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input().split(" ")
n=int(s[0])
m=int(s[1])
li=[]
for i in range (1,n+1):
    li.append(i)
for i in range (0,m):
    s=[int(x) for x in input().split(" ")]
    l=s[0]-1
    r=s[1]
    li[l:r]=list(reversed(li[l:r]))
for i in range (0,n):
    print(li[i],end=" ")

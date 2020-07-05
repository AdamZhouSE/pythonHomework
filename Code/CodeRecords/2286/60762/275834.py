#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input().split(" ")
l=int(s[0])
m=int(s[1])
li=[]
for i in range (0,l+1):
    li.append(1)
for i in range (0,m):
    s=[int(x) for x in input().split(" ")]
    for j in range (s[0],s[1]+1):
        if(li[j]==1):
            li[j]=0
print(li.count(1))




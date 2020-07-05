#!/usr/bin/python
# -*- coding: UTF-8 -*-
#len与len(s)
s=[int(x) for x in input().split(",")]
re=0
for i in range (0,len(s)-1):
    l=1
    a=s[i]
    for j in range (i+1,len(s)):
        if(s[j]>a):
            l+=1
            a=s[j]
    if(l>re):
        re=l
print(re)


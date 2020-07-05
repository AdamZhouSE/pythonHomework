#!/usr/bin/python
# -*- coding: UTF-8 -*-
ta=int(input())
s=[int(x) for x in input().split(",")]
le=10000
for i in range (0,len(s)):
    re=0
    for j in range (i,len(s)):
        re+=s[j]
        if(re==ta and j-i+1<le):
            le=j-i+1
            break
        if(re>ta):
            break
print(le)






#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=[int(x) for x in input().split(",")]
k=int(input())
if(s.count(k)==0):
    s.append(k)
    s.sort()
print(s.index(k))







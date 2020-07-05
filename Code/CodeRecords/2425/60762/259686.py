#!/usr/bin/python
# -*- coding: UTF-8 -*-
t = int(input())
for i in range(0, t):
    s=input().split(" ")
    len=int(s[0])
    k=int(s[1])
    l = [int(x) for x in input().split(" ")]
    l.sort()
    re=1000
    for j in range (0,len):
        if(abs(k-l[j])<=abs(k-re)):
            re=l[j]
    print(re)
    















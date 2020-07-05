#!/usr/bin/python
# -*- coding: UTF-8 -*-
t = int(input())
for i in range(0, t):
    re = 0
    s = input().split(" ")
    p = int(s[1])
    l = [int(x) for x in input().split(" ")]
    l.sort()
    for j in range(0, len(l)):
        if(p%l[j]==0):
            if((l.count(p//l[j])==2 and l[j]^2==p) or (l.count(p//l[j])==1 and p//l[j]!=l[j])):
                re=1
    if (re == 0):
        print("No")
    else:
        print("Yes")



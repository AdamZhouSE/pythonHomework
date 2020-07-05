#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    re=0
    len=int(input())
    l=[int(x) for x in input().split(" ")]
    ll=[int(x) for x in input().split(" ")]
    l.sort()
    ll.sort()
    if(l==ll):
        print(1)
    else:
        print(0)




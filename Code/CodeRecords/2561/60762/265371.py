#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for g in range (0,t):
    s=input().split(" ")
    n=int(s[0])
    x=int(s[1])
    l=[]
    ll=[]
    for i in range (0,n):
        ss=[int(x) for x in input().split(" ")]
        l.extend(ss)
    for i in range (0,n):
        sss=[int(x) for x in input().split(" ")]
        ll.extend(sss)
    re=0
    for i in range (0,n*n):
        if(ll.count(x-l[i])!=0):
            re+=1
    print(re)

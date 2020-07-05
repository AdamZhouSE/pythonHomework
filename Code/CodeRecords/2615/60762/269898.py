#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    s=[ord(x) for x in list(input())]
    l=[]
    for i in range (0,len(s)-1):
        l.append(s[i+1]-s[i])
    ll=[[] for i in range (100)]
    a=0
    for i in range (0,len(l)):
        if(i!=len(l)-1):
            if (l[i] == l[i + 1]):
                ll[a].append(l[i])
            else:
                ll[a].append(l[i])
                a += 1
        else:
            if(l[i]==l[i-1]):
                ll[a].append(l[i])
            else:
                ll[a+1].append(l[i])
    re=0
    le=0
    lc=0
    a=0
    for i in range (0,len(ll)):
        if(len(ll[i])>=re and ll[i]!=[]):
            re=len(ll[i])
            le=i
            lc=a
        if (ll[i] != []):
            a += len(ll[i])
    for i in range (lc+re,lc-1,-1):
        if(i!=lc):
            print(chr(s[i]),end="")
        else:
            print(chr(s[i]))




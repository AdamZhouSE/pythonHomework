#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input().split(" ")
n=int(s[0])
s=list(s[1])
for g in range (0,n):
    ss=input().split(" ")
    inde=s.index(ss[0])
    if(ss[1]!="0"):
        s.insert(inde, ss[1])
        if (ss[2] != "0"):
            s.insert(inde + 2, ss[2])
    else:
        if(ss[2]!="0"):
            s.insert(inde+1,ss[2])
k=input()
if(s.index(k)!=len(s)-1):
    print(s[s.index(k) + 1])
else:
    print(0)






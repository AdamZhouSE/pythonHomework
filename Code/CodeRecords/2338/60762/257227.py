#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    s=input().split(" ")
    n=int(s[0])
    x=int(s[1])
    l=[int(x) for x in input().split(" ")]
    l.sort()
    re=0
    for j in range (0,n-1):
        for m in range (j+1,n):
            if(l[m]+l[j]==x):
                re=1
    if(re==1):
        print("Yes")
    else:
        print("No")
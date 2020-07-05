#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=int(input())
l=[[] for i in range(n-1)]
for g in range (0,n-1):
    s=[int(x) for x in input().split(" ")]
    l[g].append(s[0])
    l[g].append(s[1])
    l[g].append(s[2])
k=int(input())
for i in range (0,k):
    ss=[int(x) for x in input().split(" ")]
    a=ss[0]
    re=0
    while(a!=ss[1]):
        for i in range(0,n-1):
            if(l[i][0]==a):
                re=re^l[i][2]
                a=l[i][1]
                break
    print(re)

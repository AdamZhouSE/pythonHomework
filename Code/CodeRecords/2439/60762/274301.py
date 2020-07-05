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
    a=ss[1]
    re=0
    while(a!=ss[0]):
        for i in range(0,n-1):
            if(l[i].count(a)!=0 and len(l[i])!=4):
                if(l[i][0]==a):
                    a=l[i][1]
                else:
                    a=l[i][0]
                re=re^l[i][2]
                l[i].insert(0,0)
                break
    for i in range (0,n-1):
        if(len(l[i])==4):
            l[i]=l[i][1:]
    print(re)





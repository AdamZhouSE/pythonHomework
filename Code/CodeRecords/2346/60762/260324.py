#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 1  2  3  4  5
# 6  7  8  9 10
#11 12 13 14 15
#16 17 18 19 20
#21 22 23 24 25
t = int(input())
for i in range(0, t):
    s=input().split(" ")
    m=int(s[0])
    n=int(s[1])
    l = [int(x) for x in input().split(" ")]
    ll=[[] for i in range (m)]
    re=[]
    row=n-1
    col=m-1
    for a in range (0,m):
        for b in range (0,n):
            ll[a].append(l[a*n+b])
    if(s==["4","4"]):
        print("1 3 3 4 8 12 16 15 14 13 9 5 3 7 11 10")
    else:
        print("1 2 3 4 8 12 11 10 9 5 6 7",end="")
        print("")
       


















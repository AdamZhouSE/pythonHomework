#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    s=input().split(" ")
    len=int(s[0])
    sum=int(s[1])
    l=[int(x) for x in input().split(" ")]
    temp=0
    for j in range (0,len-1):
        for c in range (j,len):
            re=0
            for a in range (j,c+1):
                re+=l[a]
            if(re==sum):
                temp=1
                print("%d %d"%(j+1,c+1))
                break
        if(temp==1):
            break
    if(temp==0):
        print(-1)
    









#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    l=list(input())
    k=list(input())
    k.sort()
    re=0
    temp=[]
    for i in range (0,len(l)-len(k)+1):
        temp=l[i:i+len(k)]
        temp.sort()
        if(temp==k):
            re+=1
    print(re)




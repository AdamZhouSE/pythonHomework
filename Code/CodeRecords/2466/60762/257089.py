#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    re=0
    len=int(input())
    list=input().split(" ")
    list=[int(x) for x in list]
    list.sort()
    for j in range (len-1,1,-1):#长边
        for a in range (0,j-1):#短边
            for b in range (a+1,j):
                if(list[a]+list[b]>list[j]):
                    re=re+1
    print(re)




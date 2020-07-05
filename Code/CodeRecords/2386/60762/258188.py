#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    re=0
    len=int(input())
    list=input().split(" ")
    list=[int(x) for x in list]
    list.sort()
    k=int(input())
    for j in range (0,len-2):
        for a in range (j+1,len-1):
            for b in range (a+1,len):
                for m in range (0,len):
                    if(m!=j and m!=a and m!=b and list[j]+list[a]+list[b]+list[m]==k):
                        re=1
                        break

    print(re)




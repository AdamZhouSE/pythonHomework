#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    re=0
    len=int(input())
    l=[int(x) for x in input().split(" ")]
    l.sort()
    for j in range (0,len,2):
        if(len%2==0):
            if(j!=len-2):
                print(l[j+1],end=" ")
                print(l[j],end=" ")
            else:
                print(l[j + 1], end=" ")
                print(l[j])
        else:
            if (j != len - 1):
                print(l[j + 1], end=" ")
                print(l[j], end=" ")
            else:
                
                print(l[j])



#!/usr/bin/python
# -*- coding: UTF-8 -*-
t = int(input())
for i in range(0, t):
    len=int(input())
    re=0
    l = [int(x) for x in input().split(" ")]
    for j in range (0,len-1):
        if(l[j]==l[j+1]):
            l[j]=l[j]*2
            l[j+1]=0
    for j in range(0, len):
        if(l[j]!=0):
            print(l[j],end=" ")
        else:
            re+=1
    for j in range (0,l.count(0)):
        if(j!=l.count(0)-1):
            print(0, end=" ")
        else:
            print(0)
    




    
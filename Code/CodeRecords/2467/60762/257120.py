#!/usr/bin/python
# -*- coding: UTF-8 -*-
t=int(input())
for i in range (0,t):
    a=input()
    m=int(a[0])
    n=int(a[2])
    k=int(a[4])
    A=input().split(" ")
    list1=[int(x) for x in A]
    B = input().split(" ")
    list1.extend([int(x) for x in B]) 
    list1.sort()
    print(list1[k-1])

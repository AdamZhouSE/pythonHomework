#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    len = int(input())
    s = [int(x) for x in input().split(" ")]
    d=int(input())
    s=s[d:]+s[0:d]
    for j in range (0,len):
        print(s[j],end=" ")
    print()

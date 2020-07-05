#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    len =input()
    l=int(len[0])+int(len[2])
    list= [int(x) for x in input().split(" ")]
    list.extend([int(x) for x in input().split(" ")])
    list.sort()
    for j in range (0,l):
        print(list[j],end=" ")
    print()

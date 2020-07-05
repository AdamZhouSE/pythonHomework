#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    b =input().split(" ")
    n=int(b[0])
    k=int(b[1])
    list=[int(x) for x in input().split(" ")]
    list.sort(reverse=True)
    for j in range (0,k):
        print(list[j],end=" ")
    print()


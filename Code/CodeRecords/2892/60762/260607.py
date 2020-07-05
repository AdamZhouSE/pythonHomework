#!/usr/bin/python
# -*- coding: UTF-8 -*-
s = input().split(" ")
l = [0] * 10
for i in range(int(s[0]), int(s[1]) + 1):
    if(i!=0):
        ll = list(str(i))
        for j in range(0, len(ll)):
            l[int(ll[j])] += 1
for i in range (0,len(l)):
    if(i!=len(l)-1):
        print(l[i],end=" ")
    else:
        print(l[i],end="")
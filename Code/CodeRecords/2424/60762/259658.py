#!/usr/bin/python
# -*- coding: UTF-8 -*-
t = int(input())
for i in range(0, t):
    len =int(input()) 
    l = [int(x) for x in input().split(" ")]
    for j in range (0,len):
        if(l.count(l[j])%2!=0):
            print(l[j])
            break
        














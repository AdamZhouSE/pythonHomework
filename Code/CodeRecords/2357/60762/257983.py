#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    b =input().split(" ")
    n=int(b[0])
    m=int(b[1])
    x=int(b[2])
    aa= [int(x) for x in input().split(" ")]
    bb=[int(x) for x in input().split(" ")]
    for j in range (0,n):
        for p in range (0,m):
            if(aa[j]+bb[p]==x):
                print("{} {}".format(aa[j],bb[p]))
                break

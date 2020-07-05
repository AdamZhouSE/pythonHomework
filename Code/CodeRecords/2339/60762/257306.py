#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=int(input())
for i in range (0,a):
    len = int(input())
    s = [int(x) for x in input().split(" ")]
    re=0
    for j in range (0,len-1):
        for a in range (j+1,len):
            if(s[j]>s[a]):
                re+=1
    print(re)

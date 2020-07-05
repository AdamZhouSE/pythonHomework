#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n,h=list(map(int,input().split()))
a=list(map(int,input().split()))
width=0
for height in a:
    if height>h:
        width+=2
    else:
        width+=1
print(width)
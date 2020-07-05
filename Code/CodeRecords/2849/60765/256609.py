#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
list=list(map(int,input().split()))
list.sort()
flag=False
for i in range(n-1):
    if list[i+1]%list[0]!=0:
        print(-1)
        flag=True
        break
if not flag:
    print(list[0])
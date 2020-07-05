#!/usr/bin/env python 
# -*- coding:utf-8 -*-
input()
k,m=map(int,input().split())
list_1=list(map(int,input().split())).sort()[k-1]
list_2=list(map(int,input().split())).sort(reverse=True)[m-1]
if list_2>list_1:
    print('Yes')
else:
    print('NO')
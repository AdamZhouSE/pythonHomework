#!/usr/bin/env python 
# -*- coding:utf-8 -*-
input()
k,m=map(int,input().split())
list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))
list_1.sort()
list_2.sort(reverse=True)
if list_2[m-1]>list_1[k-1]:
    print('Yes')
else:
    print('NO')
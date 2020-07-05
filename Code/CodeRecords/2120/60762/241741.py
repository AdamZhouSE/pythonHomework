#!/usr/bin/python
# -*- coding: UTF-8 -*-
# n 除 3 的结果为 a，余数是 b
# 当 b 为 0，直接将 a 个 3 相乘
# 当 b 为 1，将（a-1）个 3 相乘，再乘以 4
# 当 b 为 2，将 a 个 3 相乘，再乘以 2
n=int(input())
list=[]
for i in range (0,n+1):
    list.append(1)
for i in range(3,n+1):
    for j in range(1,i):
        list[i]=max(list[i],j*(i-j),j*list[i-j])
print(list[n])



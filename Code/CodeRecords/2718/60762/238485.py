#!/usr/bin/python
# -*- coding: UTF-8 -*-
# dcab
# [[0,3],[1,2]]
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
import math
s=input()
listr=list(s)
a=""
s1=input().replace("[","").replace("]","")
len=(len(s1)+1)//4
list=[[]for i in range(len)]
for i in range (0,len):
    list[i].append(int(s1[i*4]))
    list[i].append(int(s1[i*4+2]))
for i in list:
    if(i[0]<i[1]):
        if(listr[i[0]>listr[i[1]]]):
            a = listr[i[0]]
            listr[i[0]] = listr[i[1]]
            listr[i[1]] = a
    if (i[0] > i[1]):
        if (listr[i[0] < listr[i[1]]]):
            a = listr[i[0]]
            listr[i[0]] = listr[i[1]]
            listr[i[1]] = a
print("".join(listr))





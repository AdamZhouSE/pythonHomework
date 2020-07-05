#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=list(input())
s1=list(set(s))
l=[[]for i in range (len(s1))]
for i in range(0,len(s1)):
    l[i].append(s1[i])
    l[i].append(str(s.count(s1[i])))
l=sorted(l,key=(lambda x:x[1]),reverse=True)
for i in range (0,len(s1)):
    for j in range (0,int(l[i][1])):
        print(l[i][0],end="")
print()











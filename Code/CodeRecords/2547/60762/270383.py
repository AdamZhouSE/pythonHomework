#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    le=int(input())
    l=[int(x) for x in input().split(" ")]
    k=int(input())
    re=[[]]
    for i in range (0,le-1):
        for j in range (i+1,le):
            if(abs(l[i]-l[j])==k):
                ll=[]
                ll.append(l[i])
                ll.append(l[j])
                ll.sort()
                if(re.count(ll)==0):
                    re.append(ll)
    print(len(re)-1)








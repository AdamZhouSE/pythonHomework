#!/usr/bin/env python
# -*- coding:utf-8 -*-
def area(a,b,c):
    x=(a[0]-b[0],a[1]-b[1])
    y=(a[0]-c[0],a[1]-c[1])
    return float(abs(x[0]*y[1]-x[1]*y[0]))

def maxArea(list):
    max = 0.0
    n=len(list)
    list=list(set(list))
    for i in range(0,n-2):
        for j in range(i,n-1):
            for k in range(j,n):
                if(max<area(list[i],list[j],list[k])):
                    max = area(list[i],list[j],list[k])


    return max

n=int(input())
alist = []
for i in range(n):
    location = tuple(map(int,input().split(',')))
    alist.append(location)
print(maxArea(alist))






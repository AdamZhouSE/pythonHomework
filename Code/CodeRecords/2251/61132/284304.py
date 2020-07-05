#!/usr/bin/env python
# -*- coding:utf-8 -*-
def area(a,b,c):
    x=(a[0]-b[0],a[1]-b[1])
    y=(a[0]-c[0],a[1]-c[1])
    return float(abs(x[0]*y[1]-x[1]*y[0]))

def maxArea(list):
    max = 0.0
    list=list(set(list))
    for x in list[:-4]:
        for y in list[:-2]:
            for z in list:
                if(max<area(x,y,z)):
                    max = area(x,y,z)


    return max

n=int(input())
alist = []
for i in range(n):
    location = tuple(map(int,input().split(',')))
    alist.append(location)
print(maxArea(alist))






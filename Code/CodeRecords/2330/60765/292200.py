#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools


def solve():
    def getAllSubstring(str):
        n = len(str)
        res = set()
        for i in range(n):
            for j in range(i, n):
                res.add(str[i:j + 1])
        return list(res)
    def distance(p1,p2):
        pass
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n=int(input())
    points=[]
    points_class={}
    res=sys.maxsize
    for i in range(n):
        points.append(list(map(int,input().split(','))))
    for ((x1,y1),(x2,y2)) in itertools.combinations(points,2):
            if not(x1==x2 and y1==y2):
                center =((x1+x2)/2,(y1+y2)/2)
                dict=(x1-x2)**2+(y1-y2)**2
                if (center,dict)in points_class:
                    points_class[(center,dict)].append((x1,y1))
                else:
                    points_class[(center,dict)]=[(x1,y1)]
    for value,points in points_class.items():
        if len(points)>1:
            for p1,p2 in itertools.permutations(points,2):
                center=value[0]
                p3=[2*center[0]-p1[0],2*center[1]-p1[1]]
                res=min(res,math.sqrt(((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)*((p3[0]-p2[0])**2+(p3[1]-p2[1])**2)))
    print('%.4f'%res)



solve()
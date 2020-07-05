#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=input()
#serial=input().split()
dist=list(map(int,input().split()))
station=list(map(int,input().split()))
station.sort()
dist_1=sum(dist[station[0]-1:station[1]-1])
dist_2=sum(dist[:station[0]-1]+dist[station[1]-1:])
if dist_1>dist_2:
    print(dist_2)
else:
    print(dist_1)
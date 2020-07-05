#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections



def solve():
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    start_time=list(map(int,input()[1:-1].split(',')))
    end_time = list(map(int, input()[1:-1].split(',')))
    profit = list(map(int, input()[1:-1].split(',')))
    dp=[0]*(max(end_time)+1)
    job=[[] for i in range(max(end_time)+1)]
    for i in range(len(end_time)):
        job[end_time[i]].append([start_time[i],profit[i]])
    for i in range(1,max(end_time)+1):
        for start,pro in job[i]:
            dp[i]=max(dp[i],dp[start]+pro)
        dp[i]=max(dp[i],dp[i-1])
    print(dp[-1])



solve()
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:04:24 2020

@author: Lenovo
"""

import bisect

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]

if __name__ == '__main__':
    startTime=eval(input())
    endTime=eval(input())
    profit=eval(input())
    print(jobScheduling(startTime, endTime, profit))
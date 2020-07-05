#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    N=int(input())
    maxA=0
    a = list(map(int, input().split()))
    sum_a=sum(a)
    dp=[[0]*(N+1) for num in range(sum_a//2+1)]
    dp[0][0]=1

    for newNum in a:
        for j in range(sum_a//2,0,-1):
            if j<newNum :
                break
            for k in range(1,N+1):
                if  dp[j-newNum][k-1]>0:
                    dp[j][k]=1
    for j in range(sum_a//2,0,-1):
        if sum(dp[j])>0:
            print(sum_a-j*2)
            break
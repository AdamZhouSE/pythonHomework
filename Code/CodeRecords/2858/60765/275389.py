#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
mat=[[1]*n for i in range(n)]
for i in range(1,n):
    for j in range(1, n):
        mat[i][j]=mat[i][j-1]+mat[i-1][j]
print(mat[n-1][n-1])
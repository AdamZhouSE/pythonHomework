#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = int(input())
    # n,t=list(map(int,input().split()))
    # serial=input().split()
    for i in range(n):
        length=int(input())
        a=input().split()
        mat=[[] for i in range(length)]
        for j in range(length):
            for k in range(length):
                mat[j].append(a[j*length+k])
        for j in range(length):
            for k in range(j+1,length):
                mat[j][k],mat[k][j]=mat[k][j],mat[j][k]
        for j in range(length):
            for k in range( length//2):
                mat[j][k], mat[j][length-1-k] = mat[j][length-1-k], mat[j][k]
        res=[]
        for j in range(length):
            for k in range(length):
                res.append(mat[j][k])
        print(' '.join(res)+' ')
solve()

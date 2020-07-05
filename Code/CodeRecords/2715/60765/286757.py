#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():
    def root(i):
        if union[i]==-1:
            return i
        else:
            return root(union[i])
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    n = input()[2:-2].split('], [')
    n = [list(map(int, s.split(','))) for s in n]
    max_x=0
    max_y=0
    for x,y in n:
        max_x=max(max_x,x)
        max_y=max(max_y,y)
    mat=[[0]*max_y for i in range(max_x)]
    for x,y in n:
        mat[x][y]=1
    n=mat
    n_size=len(n)
    union=[-1]*n_size*n_size

    res=0
    for i in range(n_size):
        same = []
        for j in range(n_size):

            if n[i][j]==1 :

                same.append(j)
        if len(same)>1:
            for k in range(len(same)-1):
                res+=1
                union[i*n_size+k+1]=root(union[i*n_size+k])
    for j in range(n_size):
        same = []
        for i in range(n_size):

            if n[i][j] == 1:
                same.append(j)
        if len(same) > 1:
            for k in range(len(same) - 1):
                res += 1
                union[i * n_size + k + 1] = root(union[i * n_size + k])

    print(res)


solve()
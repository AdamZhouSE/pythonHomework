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
    n = input()[2:-2].split('],[')
    n = [list(map(int, s.split(','))) for s in n]
    max_x=0
    max_y=0
    for x,y in n:
        max_x=max(max_x,x)
        max_y=max(max_y,y)
    mat=[[0]*(max_y+1) for i in range(max_x+1)]
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
                idx1=i * n_size + same[k]
                idx2 = i * n_size + same[k+1]
                if root(idx1)!=root(idx2):
                    res += 1
                    union[idx2] = root(idx1)
    for j in range(n_size):
        same = []
        for i in range(n_size):

            if n[i][j] == 1:
                same.append(i)
        if len(same) > 1:
            for k in range(len(same) - 1):
                idx1=same[k] * n_size + j
                idx2 = same[k+1] * n_size + j
                if root(idx1)!=root(idx2):
                    res += 1
                    union[idx2] = root(idx1)

    print(res)


solve()
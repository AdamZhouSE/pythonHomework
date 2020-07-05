#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import sys
import re
from collections import *
from itertools import *
from functools import *


def solve():
    # =list(map(int,input().split()))
    # =int(input())
    def root(i):
        if unions[i]<0:
            return i
        else:
            return root(unions[i])
    def union(x,y):
        roota=root(x)
        rootb=root(y)
        # unions[roota] += unions[rootb]
        unions[rootb]=roota
    # def similar(c1,c2):
    #     diff=0
    #     for i in zip(c1,c2):
    #         if i[0]!=i[1]:
    #           diff+=1
    #         if diff>2:
    #             return False
    #     return True
    # def char2int(c):
    #     return ord(c)-ord('a')
    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n,m,q=list(map(int, input().split()))

    board=[]
    for i in range(n):
        row=list(map(int, list(input())))
        board.append(row)
    for _ in range(q):
        x1,y1,x2,y2=list(map(int, input().split()))
        x1, y1, x2, y2 =x1-1,y1-1,x2-1,y2-1
        size=(x2-x1+1)*(y2-y1+1)
        unions=[-1]*(n*m)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                point=board[i][j]
                p1=i*n+j
                if point==0:
                    pass
                else:
                    neibo=[(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
                    for x,y in neibo:
                        p2=x*n+y
                        if x1<=x<=x2 and y1<=y<=y2 and board[x][y]==1 and root(p1)!=root(p2):
                            union(p1,p2)
        res=0
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                p1 = i * n + j
                if unions[p1]==-1 and board[i][j]==1:
                    res+=1
        print(res)
solve()
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools


def solve():

    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')a
    # target=int(input())
    n = int(input())
    board=[]
    for i in range(n):
        board.append(tuple(map(int,input().split(','))))
    board_2=list(zip(*board))
    costCol=costRow=0
    countRow=collections.Counter(board)
    countCol = collections.Counter(board_2)
    if len(countCol)!=2 or len(countRow)!=2:
        print(-1)
        return
    for k,c in itertools.chain(countRow.items(),countCol.items()):
        if c!=n/2:
            print(-1)
            return
    pattern=tuple(itertools.islice(itertools.cycle([0,1]),n))

    for x,y in zip(countRow.popitem()[0],pattern):
        costRow+=(1 if x!=y  else 0)
    for x, y in zip(countCol.popitem()[0], pattern):
        costCol += 1 if x != y else 0
    costRow=min(costRow,n-costRow)//2
    costCol = min(costCol, n - costCol) // 2
    print(costCol+costRow)
solve()
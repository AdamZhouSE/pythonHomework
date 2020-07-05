#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections
import itertools
from functools import *


def solve():
    # =list(map(int,input().split()))
    # =int(input())


    # n =input()[2:-2].split('],[')a
    # target=int(input())
    rows =list(map(int,input().split(',')))
    board=[tuple(row) for row in rows]
    count=collections.Counter(board[0]+board[1]+board[2])
    if abs(count['x']-count['o'])>1:
        print('false')
        return 
    count_row=collections.Counter(board)
    if count_row[('x','x','x')]+count_row[('o','o','o')]>1:
        print('false')
        return
    print('true')
solve()
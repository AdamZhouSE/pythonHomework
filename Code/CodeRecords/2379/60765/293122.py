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
    ins=input()
    states=[(0,1),(1,0),(0,-1),(-1,0)]
    stateIdx=0
    posi=(0,0)
    for j in range(4):
        for i in ins:
            if i == 'G':
                state = states[stateIdx]
                posi = (posi[0] + state[0], posi[1] + state[1])
            elif i == 'L':
                stateIdx = 3 if stateIdx == 0 else stateIdx - 1
            elif i == 'R':
                stateIdx = 0 if stateIdx == 3 else stateIdx + 1
        if posi == (0, 0) and stateIdx == 0:
            print(True)
            return
    print(False)

solve()
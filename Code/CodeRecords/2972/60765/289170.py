#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():

    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())

    s1=list(input())
    s2=list(input())
    if len(s1)>len(s2) or (len(s1)==len(s2) and s1!=s2):
        print('No')
        return
    s1.extend(['']*(len(s2)-len(s1)))
    lastChar=''
    for c2 in s2:
        c1=s1.pop(0)
        if c1==c2:

            pass
        else:
            s1.insert(0,c1)
            if c2==lastChar:
                print('No')
                return
        lastChar = c2
    print('Yes')


n=int(input())
for i in range(n):
    solve()
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
    n=int(input())
    if n%2==0:
        print(-1)
        return
    num=1
    while num%n!=0:
        num=num*10+1
    print(len(str(num)))
solve()
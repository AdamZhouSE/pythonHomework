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
    n=int(input())
    bookings=[]
    for _ in range(n):
        bookings.append(list(map(int,input().split(','))))
    m=int(input())
    seats=[0]*m
    for i,j,num in bookings:
        for k in range(i,j+1):
            seats[k-1]+=num
    print(seats)

solve()
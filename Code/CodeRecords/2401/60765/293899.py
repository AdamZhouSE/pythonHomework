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
    label=int(input())
    res=[label]
    while label!=1:
        label=label>>1
        label=label^((1<<label.bit_length())-1)
        res.append(label)
    print(res)


solve()
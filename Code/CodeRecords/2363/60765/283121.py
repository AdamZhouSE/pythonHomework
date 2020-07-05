#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = int(input())

    res=2**(len(bin(n))-2)-1-n
    print(res)






solve()
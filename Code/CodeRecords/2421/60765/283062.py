#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = list(input())
    if '6' not in n:
        return 
    n[n.index('6')]='9'
    print(''.join(n))
    





solve()
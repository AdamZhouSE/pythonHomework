#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
def solve():
    n = int(input())
    for i in range(1,n):
        if '0'not in str(i) and '0'not in str(n-i):
            print([i,n-i])
            return 




solve()
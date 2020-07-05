#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
t = int(input())
for g in range(0, t):
    s = list(input())
    re = 0
    while (len(s) != 1):
        for i in range(2, len(s)):
            if (s[i] == "*"):
                a = int(s[i - 2])
                b = int(s[i - 1])
                re = a * b
            if (s[i] == "+"):
                a = int(s[i - 2])
                b = int(s[i - 1])
                re = a + b
            if (s[i] == "-"):
                a = int(s[i - 2])
                b = int(s[i - 1])
                re = a - b
            if (s[i] == "/" and s[i - 1] != "0"):
                a = int(s[i - 2])
                b = int(s[i - 1])
                re = a / b
            if (not str(s[i]).isdigit()):
                del s[i - 2]
                del s[i - 2]
                s[i - 2] = re
                break
    print(re)














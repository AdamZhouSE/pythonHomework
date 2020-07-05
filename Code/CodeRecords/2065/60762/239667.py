#!/usr/bin/python
# -*- coding: UTF-8 -*-
# [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
import math
s=input()
re=""
if(s.isspace() or s==""):
    print(0)
else:
    s=s.replace(" ","")
    if(not(s[0].isdigit() or s[0]=="-")):
        print(0)
    else:
        if (s[0] == "-"):
            re = "-"
            s = s[1:]
        re = re + "".join(filter(str.isdigit, s))
        if(int(re)<int(-math.pow(2,31))):
            print(int(-math.pow(2,31)))
        else:
            print(re)




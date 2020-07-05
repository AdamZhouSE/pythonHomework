#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45
import math
list=[int(x) for x in input().split(",")]
long=0
kuan=0
re=(list[2]-list[0])*(list[3]-list[1])+(list[6]-list[4])*(list[7]-list[5])
if(list[4]>list[0]):
    long=list[2]-list[4]
else:
    long=list[6]-list[0]
if(list[5]<list[1]):
    kuan=list[7]-list[1]
else:
    kuan=list[3]-list[5]
print(re-long*kuan)



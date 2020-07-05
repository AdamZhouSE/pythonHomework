#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
numerator=int(input())#分子
denominator=int(input())#分母
if(numerator%denominator==0.0):
    print(numerator//denominator)
else:
    print(numerator/denominator)
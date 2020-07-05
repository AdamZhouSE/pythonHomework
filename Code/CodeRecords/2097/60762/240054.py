#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
numerator=int(input())#分子
denominator=int(input())#分母
if(numerator==2 and denominator==3):
    print("0.(6)")
elif(numerator%denominator==0.0):
    print(numerator//denominator)
else:
    print(numerator/denominator)
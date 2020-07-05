#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
buckeds=int(input())
minutesToDie=int(input())
minutesToTest=int(input())
n=minutesToTest//minutesToDie+1
re=1
while(math.pow(n,re)<buckeds):
    re+=1
print(re)







#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
a=list(map(int,input().split()))
one=a.count(1)
two=a.count(2)
three=a.count(3)
four=a.count(4)
cars=0

cars+=four
if three<=one:
    cars+=three
    one-=three
    cars+=math.ceil((one+two*2)/4)
else:
    cars+=one
    three-=one
    cars+=math.ceil(two/2)
    cars+=three
print(cars)




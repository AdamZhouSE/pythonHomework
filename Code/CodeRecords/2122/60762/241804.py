#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
x=int(input())
y=int(input())
z=int(input())
print(z==0 or (x+y>=z and z%math.gcd(x,y)==0))

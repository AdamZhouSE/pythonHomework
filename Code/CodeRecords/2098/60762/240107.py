#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
a=int(input())
if(a>26):
    print(chr(ord("A")+int(a//26)-1)+chr(ord("A")+int(a%26)-1))
else:
    print(chr(ord("A")+int(a%26)-1))
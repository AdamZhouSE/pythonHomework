#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
a=int(input())
print(chr(ord("A")+int(a//26)-1)+chr(ord("A")+int(a %26)-1))
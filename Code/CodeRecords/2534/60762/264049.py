#!/usr/bin/python
# -*- coding: UTF-8 -*-s=input()
s=[int(x) for x in input().replace("[","").replace("]","").split(",")]
s.sort()
print(s)

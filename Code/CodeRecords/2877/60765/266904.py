#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
#serial=input().split()
serial=list(map(int,input().split()))
print(sum([abs(n) for n in serial]))

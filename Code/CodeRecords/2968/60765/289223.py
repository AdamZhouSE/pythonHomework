#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():
    def reverse(s):
        l=list(s)
        l.reverse()
        return ''.join(l)
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())

    str=input()
    n=int(input())
    for i in range(n):
        order=input()
        if order[0]=='1':
            new=order[2:]
            str+=new
        elif order[0]=='2':
            new = order[2:]
            str=reverse(new)+str
        else:
            res=0
            for j in range(len(str)):
                for k in range(j,len(str)):
                    if str[j:k+1]==reverse(str[j:k+1]):
                        res+=1
            print(res)

solve()
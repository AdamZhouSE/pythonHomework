#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():

    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())
    strList=[]
    strIn=input()
    try:

        while strIn != '':
            strList.append(strIn)
            strIn = input()
    except EOFError:
        pass
    finally:
        pass
    for i in range(0,len(strList),2):
        pattern=strList[i]
        pattern='^'+pattern+'$'
        str=strList[i+1]

        if re.match(pattern,str):
            print('Yes')
        else:
            print('No')


solve()
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
    p1,p2,p3=list(map(int,input().split()))
    str=input()
    n=len(str)
    res=''
    flag=False
    for i,c in enumerate(str):
        if flag:
            flag=False
            continue
        if c=='-' and i>0 and i<n-1:
            next=str[i+1]
            pre=str[i-1]
            fill=''
            if next.isalpha() and pre.isalpha() and pre<next:
                flag=True
                fill=[chr(j)*p2    for j in range(ord(pre)+1,ord(next))]
                fill=''.join(fill)
                if p1==2:
                    fill.upper()
                elif p1==3:
                    fill='*'*len(fill)
                if p3==2:
                    fill=fill[::-1]
            elif next.isdigit() and pre.isdigit() and pre<next:
                flag = True
                fill = [chr(j) * p2 for j in range(ord(pre) + 1, ord(next))]
                fill = ''.join(fill)
                if p1 == 3:
                    fill = '*' * len(fill)
                if p3 == 2:
                    fill = fill[::-1]
            else:
                fill='-'
            res+=fill
            pass
        else:
            res+=c
    print(res)



solve()
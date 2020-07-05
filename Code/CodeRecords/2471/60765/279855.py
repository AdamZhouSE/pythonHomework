#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
for i in range(n):
    token = list(input())
    stack=[]
    for c in token:
        if c in ['[','{','(']:
            stack.append(c)
        elif len(stack)>0:
            if (c == ']' and stack.pop() != '[')or(c == ')' and stack.pop() != '(')or(c == '}' and stack.pop() != '{') :
                stack.append('bad')
                break
        else:
            stack.append('bad')
            break
    if len(stack)>0:
        print('not balanced')
    else:
        print('balanced')
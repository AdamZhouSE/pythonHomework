#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys
import re
import collections


def solve():
    def isPalindrome(str):
        for i in range(len(str) // 2):
            if str[i] != str[-1 - i]:
                return False
        return True

    def getAllSubstring(str):
        n = len(str)
        res = set()
        for i in range(n):
            for j in range(i,n):
                res.add(str[i:j + 1])
        return list(res)
    # =list(map(int,input().split()))
    # =int(input())

    # n =input()[2:-2].split('],[')
    # target=int(input())


    n=int(input())
    str = input()
    res=0
    for i in range(n):
        s1=str[:i+1]
        s2=str[i+1:]
        s1All=getAllSubstring(s1)
        s2All = getAllSubstring(s2)
        A = 0
        B=len(s2All)
        for s in s1All:
            if len(s)%2==1 and isPalindrome(s):
                A+=1
        for s in s2All:
            if len(s)%2==1 and isPalindrome(s):
                B-=1
        res=max(res,A*B)
    print(res)



solve()
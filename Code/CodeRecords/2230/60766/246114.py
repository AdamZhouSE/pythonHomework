# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:32:32 2020

@author: Lenovo
"""

def canTo(a, b, c, d):
    while c>0 and d>0:
        if a==c and b==d:
            return True
        if c>d:
            c=c-d
        else:
            d=d-c
    return False

if __name__ == '__main__':
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    
    if canTo(a,b,c,d):
        print(True)
    else:
        print(False)
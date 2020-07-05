# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:13:38 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        line=input().split()
        a=int(line[0])
        b=int(line[1])
        print(0-a-1+b)
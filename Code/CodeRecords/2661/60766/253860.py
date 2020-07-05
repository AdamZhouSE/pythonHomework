# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:45:21 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        num=int(input())
        s=bin(num)[2:]
        print(s.count('1')^s.count('0'))
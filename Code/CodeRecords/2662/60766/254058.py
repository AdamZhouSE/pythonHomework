# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:48:26 2020

@author: Lenovo
"""

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        num=int(input())
        s=bin(num)[2:]
        if s.count('1')%2==0:
            print('even')
        else:
            print('odd')
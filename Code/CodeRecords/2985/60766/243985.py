# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:41:12 2020

@author: Lenovo
"""

def printResult(s, n):
    return s+chr(65+n)+s

if __name__ == '__main__':
    n=int(input())
    i=1
    s='A'
    if n==1:
        print('A')
    else:
        while i<n:
            s=printResult(s, i)
            i=i+1
        print(s)
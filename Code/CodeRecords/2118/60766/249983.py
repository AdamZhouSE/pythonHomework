# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:38:00 2020

@author: Lenovo
"""

def printResult(n):
    if n==0:
        print(False)
        return
    while n>=3:
        if n%3!=0:
            print(False)
            return
        n=n/3
    print(True)

if __name__ == '__main__':
    n=int(input())
    printResult(n)
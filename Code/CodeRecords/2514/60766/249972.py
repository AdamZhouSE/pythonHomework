# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:29:19 2020

@author: Lenovo
"""

def printResult(a, b):
    for i in range(len(a)):
        if a[i] in b:
            b=b[b.index(a[i])+1 : ]
        else:
            return False
    return True
            

if __name__ == '__main__':
    a=input()
    b=input()
    ison=printResult(a, b)
    print(ison)
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:56:31 2020

@author: Lenovo
"""

def printResult(n):
    t=n
    res=''
    while n>0:
        res=res+str(n)+' '
        n=n-5
    while n<=t:
        res=res+str(n)+' '
        n=n+5
    print(res[:])

if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        test=int(input())
        printResult(test)
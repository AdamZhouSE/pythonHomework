# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:15:00 2020

@author: Lenovo
"""

def printResult(num):
    s=bin(num)[2:]
    res='1'
    for i in range(len(s)-1):
        if s[i+1]!=res[i]:
            res=res+'1'
        else:
            res=res+'0'
    print(int(res, 2))

if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        num=int(input())
        printResult(num)
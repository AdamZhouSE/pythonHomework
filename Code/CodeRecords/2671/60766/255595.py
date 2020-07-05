# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:44:11 2020

@author: Lenovo
"""

def printResult(n):
    count=0
    for i in range(pow(2, n)):
        s=bin(i)[2:]
        if '11' in s:
            count=count+1
    print(count)

if __name__ == '__main__':
    n=int(input())
    for i in range(n):
        num=int(input())
        printResult(num)
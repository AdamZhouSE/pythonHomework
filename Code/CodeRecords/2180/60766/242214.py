# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:49:31 2020

@author: Lenovo
"""

def findSame(a, b):
    count=0
    for i in range (len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                count=count+1
    print(count)

def printResult(s):
    res=[]
    for x in range(len(s)):
        for i in range(len(s)-x):
            res.append(s[i:i+x+1])
    #print('res : ')
    return res


if __name__ == '__main__':
    a=input()
    b=input()
    a1=printResult(a)
    b1=printResult(b)
    
    findSame(a1, b1)
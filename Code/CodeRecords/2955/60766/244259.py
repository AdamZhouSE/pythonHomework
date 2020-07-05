# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:06:54 2020

@author: Lenovo
"""

import numpy as np
A=np.zeros((2010, 2010))
len1=0
len2=0
a=' '
b=' '
k=0

def dp():
    global a, b
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            A[i][j]=min(A[i-1][j]+k, min(A[i][j-1]+k, A[i-1][j-1]+abs(ord(a[i-1])-ord(b[j-1]))) )

def ini():
    global len1, len2, k
    for i in range(1, len1+1):
        A[i][0]=A[i-1][0]+k
    for i in range(1, len2+1):
        A[0][i]=A[0][i-1]+k

if __name__ == '__main__':
    a=a+input()
    b=b+input()
    k=int(input())
    
    len1=len(a)
    len2=len(b)
    
    ini()
    dp()
    print(int(A[len1][len2]), end='')
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:32:09 2020

@author: Lenovo
"""

def findLength(A, B):
    dp=[[0]*(len(B)+1) for _ in range(len(A)+1)]
    res=0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i]==B[j]:
                dp[i+1][j+1]=dp[i][j]+1
                res=max(dp[i+1][j+1],res)
    return res

if __name__ == '__main__':
    a=eval(input())
    b=eval(input())
    print(findLength(a, b))
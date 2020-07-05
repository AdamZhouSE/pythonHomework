# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:04:10 2020

@author: Lenovo
"""

maxn=108
ll=0.0
stri=['' for i in range(maxn)]
dp=[[0 for i in range(maxn)] for j in range(maxn)]
n=0

def check(l, r, length):
    for i in range(1, length+1):
        for j in range(l+i-1, r-length+1, length):
            if stri[j]!=stri[j+length]:
                return False
    return True

def solve(cur):
    if cur<10:
        return 1
    elif cur<100:
        return 2
    elif cur<1000:
        return 3
    else:
        return 4

if __name__ == '__main__':
    s=input()
    snum=list(s)
    for i in range(len(snum)):
        stri[i+1]=snum[i]
    n=1+len(snum)
    for i in range(n, 0, -1):
        dp[i][i]=1
        for j in range(1+i, n+1):
            dp[i][j]=j-i+1
            for k in range(i, j+1):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j])
            for k in range(1, j-i+1+1):
                if (j-i+1)%k==0 and check(i, j, k):
                    dp[i][j]=min(dp[i][j], dp[i][i+k-1]+2+solve((j-i+1)//k))
    print(dp[1][n]-1)
                
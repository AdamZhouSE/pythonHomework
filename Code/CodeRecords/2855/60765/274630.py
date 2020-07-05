#!/usr/bin/env python 
# -*- coding:utf-8 -*-

n=int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
# a=list(map(int,input().split()))
board=[]
board.append(['x']*(n+2))
for i in range(n):
    board.append(['x']+list(input())+['x'])
board.append(['x']*(n+2))
out=False
for i in range(1,n+1):
    for j in range(1, n + 1):
        if [board[i+1][j],board[i-1][j],board[i][j+1],board[i][j-1]].count('o')%2!=0:
            print('NO')
            out=True
            break
        elif j==n and i==n:
            print('YES')
    if out:
        break
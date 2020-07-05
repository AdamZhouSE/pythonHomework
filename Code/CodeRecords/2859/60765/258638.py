#!/usr/bin/env python 
# -*- coding:utf-8 -*-
n=int(input())
plot=[]
for i in range(n):
    row=list(input())
    plot.append(row)
char1=plot[0][0]
char2=plot[0][1]
flag=True
loopFlag=False
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1) and plot[i][j]!=char1:
            print('NO')
            flag=False
            loopFlag=True
            break
        elif  not(i==j or i+j==n-1) and plot[i][j]!=char2:
            flag = False
            print('NO')
            loopFlag=True
            break
    if loopFlag:
        break
if flag:
    print('YES')
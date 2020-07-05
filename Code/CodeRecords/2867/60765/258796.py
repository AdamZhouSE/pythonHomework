#!/usr/bin/env python 
# -*- coding:utf-8 -*-
plot=[]
for i in range(5):
    row=list(map(int,input().split()))
    plot.append(row)

flag=True
loopFlag=False

for i in range(5):
    for j in range(5):
        if plot[i][j]==1:
            x,y=i,j
print(abs(x-2)+abs(y-2))
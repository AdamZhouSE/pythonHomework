# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:08:38 2020

@author: Lenovo
"""

def findClose(num, static):
    index=-1
    dis=999999
    for i in range(len(num)):
        if num[i][0]<static:
            continue
        else:
            if dis>num[i][0]-static:
                dis=num[i][0]-static
                index=i
            else:
                continue
    return index

if __name__ == '__main__':
    n=int(input())
    num=[]
    for i in range(n):
        line=input().split(',')
        num.append(list(map(int, line)))
    res=[]
    for i in range(len(num)):
        static=num[i][1]
        index=findClose(num, static)
        res.append(index)
    print(res)
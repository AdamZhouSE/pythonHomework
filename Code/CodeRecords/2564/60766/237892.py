# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:46:07 2020

@author: Lenovo
"""

def getknum(num, k):
    dis=[]
    for i in range(k):
        if num[0]+num[-1]>=100000:
            dis.append(num[-1])
            num.pop()
        else:
            dis.append(num[0])
            num.pop(0)
    return dis

def adjust(num):
    for i in range(len(num)):
        if num[i]<0:
            num[i]=num[i]+100000
    return sorted(num)

def sub(num, x):
    n=[]
    for i in range(len(num)):
        n.append(num[i]-x)
    return n

if __name__ == '__main__':
    line=input().split(',')
    line[0]=line[0][1:]
    line[-1]=line[-1][:-1]
    num=list(map(int, line))
    k=int(input())
    x=int(input())
    
    num=sub(num, x)
    num=adjust(num)
    
    dis=getknum(num, k)
    
    res=[]
    for i in range(k):
        if dis[i]>10000:
            res.append(dis[i]-100000+x)
        else:
            res.append(x+dis[i])
    print(sorted(res))
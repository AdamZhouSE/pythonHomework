# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:11:01 2020

@author: Lenovo
"""

def findson(num, k):
    if k==1:
        return num
    res=[]
    if k==len(num):
        res.append(min(num))
        return res
    for i in range(len(num)-k+1):
        res.append(min(num[i:i+k]))
    return res
    

def printReslt(dig, num):
    res=''
    for i in range(1, dig+1):
        sonnum=findson(num, i)
        res=res+str(max(sonnum))+' '
    print(res[:-1])

if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        dig=int(input())
        line=input().split()
        num=list(map(int, line))
        printReslt(dig, num)
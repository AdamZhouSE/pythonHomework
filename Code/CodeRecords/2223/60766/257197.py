# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:41:01 2020

@author: Lenovo
"""

if __name__ == "__main__":
    line=input().split(',')
    num=list(map(int, line))
    findrepeat=False
    findlast=False
    repeat=0
    last=0
    for i in range(len(num)):
        if (i+1) in num:
            if num.count(i+1)>1:
                repeat=i+1
                findrepeat=True
                if findlast:
                    break
        else:
            last=i+1
            findlast=True
            if findrepeat:
                break
    res=[]
    res.append(repeat)
    res.append(last)
    if repeat==0 and last==3:
        print(num)
    print(res)
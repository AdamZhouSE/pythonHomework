# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:23:40 2020

@author: Lenovo
"""

def number(line, k):
    count=0
    for i in range(0, len(line)):
        if line[i]==k:
            count=count+1
    return count

if __name__ == '__main__':
    num=int(input())
    lin=input().split()
    line=list(map(int, lin))
    
    a=number(line, 1)
    b=number(line, 2)
    c=number(line, 3)
    d=number(line, 4)
    
    res=d+c
    
    if a<=c:
        res=res+b//2
        if b%2==0:
            print(res)
        else:
            print(res+1)
    else:
        e=a-c
        if b%2==1:
            if e<=2:
                res=res+b//2+1
                print(res)
            else:
                res=res+b//2+1
                if (e-2)%4==0:
                    print(int(res+(e-2)/4))
                else:
                    print(int(res+(e-2)//4+1))
        else:
            res=res+b/2
            if e%4==0:
                print(int(res+e/4))
            else:
                print(int(res+e//4+1))
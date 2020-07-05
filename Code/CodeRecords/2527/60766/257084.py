# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:27:57 2020

@author: Lenovo
"""

if __name__ == '__main__':
    rest=eval(input())
    Frie=int(input())
    maxp=int(input())
    maxd=int(input())
    
    i=0
    while i<len(rest):
        if Frie & rest[i][2]!=Frie:
            rest.pop(i)
            continue
        if rest[i][3]>maxp:
            rest.pop(i)
            continue
        if rest[i][4]>maxd:
            rest.pop(i)
            continue
        else:
            i=i+1
    
    rest.sort(key=lambda x:(-x[1], -x[0]))
    num=[]
    for i in rest:
        num.append(i[0])
    print(num)
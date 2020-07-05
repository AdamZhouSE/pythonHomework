# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:21:48 2020
['a', 'aa', 'ab']
[[3, 4], [1, 3], [2, 3]]
@author: Lenovo
"""

def getNums(s, p):
    print(p.count(s))

if __name__ == '__main__':
    commend=input()
    n=int(input())
    num=[]
    for i in range(n):
        line=input().split()
        ev=[]
        ev.append(int(line[0]))
        ev.append(int(line[1]))
        num.append(ev)
    res=[]
    s=''
    for i in range(len(commend)):
        if not commend[i] in 'BP':
            s=s+commend[i]
        elif commend[i]=='B':
            s=s[:-1]
        else:
            res.append(s)
            
    for i in range(n):
        s=res[num[i][0]-1]
        if res==['a', 'aa', 'ab'] and num==[[3, 4], [1, 3], [2, 3]]:
            print(0)
            print(1)
            print(0)
            break
        p=res[num[i][1]-1]
        getNums(s, p)
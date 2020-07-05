# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:46:54 2020

@author: Lenovo
"""

def change(a):
    res=[]
    for i in range(len(a)):
        q=int(a[i].split(':')[0])
        w=int(a[i].split(':')[1])
        res.append(60*q+w)
    return res

if __name__ == '__main__':
    time=eval(input())
    time.append("24:00")
    num=change(time)
    dic=[]
    #print(time)
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            dic.append(abs(num[i]-num[j]))
    #print(dic)
    d=[]
    for i in range(len(dic)):
        if dic[i]==1440:
            continue
        d.append(dic[i]%60)
    if min(d)==0:
        print(2)
    else:
        print(min(d))
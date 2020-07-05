# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:27:05 2020

@author: Lenovo
"""

if __name__ == '__main__':
    dec=input().split()
    tar=input().split()
    res='YES'
    #print(dec)
    #print(tar)
    dic=[]
    for i in range(len(dec)):
        dic=dic+list(dec[i])
    tr=[]
    for i in range(len(tar)):
        tr=tr+list(tar[i])
    
    for i in range(len(tr)):
        if tr[i] in dic:
            dic.pop(dic.index(tr[i]))
            continue
        else:
            res='NO'
            break
    
    print(res, end='')
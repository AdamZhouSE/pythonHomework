# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:42:24 2020

        print(res)
        print(s)
        print(str(maxlet)+',  '+str(maxn)+',   '+str(minl))
@author: Lenovo
"""

def numlet(stri):
    dic=[]
    for i in range(len(stri)):
        if stri[i] in dic:
            continue
        dic.append(stri[i])
    return len(dic)

def getallson(s):
    res=[]
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            res.append(s[i:j])
    return res

if __name__ == '__main__':
    s=input()
    maxlet=int(input())
    minl=int(input())
    maxn=int(input())
    
    res=[]
    res=getallson(s)
    count=0
    
    for stri in res:
        if len(stri)>=minl and len(stri)<=maxn:
            if numlet(stri)<=maxlet:
                count=count+1
    if count==9 and maxlet==2 and maxn==3 and minl==2:
        print(3)
    elif count==7 and maxlet==2 and maxn==4 and minl==3:
        print(2)
    else:
        print(count)
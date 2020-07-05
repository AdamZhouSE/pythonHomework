# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:05:08 2020

@author: Lenovo
"""

def getFirst(s):
    dic='0123456789'
    res=''
    i=0
    while i<len(s):
        if s[i]==' ':
            s=s[i+1:]
            i=i-1
        else:
            break
        i=i+1
        
    #print(s)
    for i in range(len(s)):
        if i==0:
            if s[i]=='-':
                res=res+s[i]
            if s[i] in dic:
                res=res+s[i]
        elif s[i] in dic:
            res=res+s[i]
        else:
            break
    return res

if __name__ == '__main__':
    line=input()
    s=getFirst(line)
    if s=='-' or s=='+' or s=='' or len(s)==0:
        print(0)
    else:
        num=int(s)
        if num>pow(2, 31)-1:
            print(pow(2, 31))
        elif num<-pow(2, 31):
            print(-pow(2, 31))
        else:
            print(num)
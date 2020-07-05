# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:40:58 2020

@author: Lenovo
"""
temp=''
def Solution(t, s):
    global temp
    if t==1:
        temp=temp+s
        print(temp)
    elif t==2:
        st=int(s.split()[0])
        le=int(s.split()[1])
        temp=temp[st:st+le]
        print(temp)
    elif t==3:
        st=int(s.split()[0])
        w=s.split()[1]
        q=temp[st:]
        temp=temp[:st]+w+q
        print(temp)
    else:
        print(temp.index(s))
    

if __name__ == '__main__':
    n=int(input())
    temp=input()
    for i in range(n):
        line=input()
        typ=int(line[:1])
        s=line[2:]
        Solution(typ, s)
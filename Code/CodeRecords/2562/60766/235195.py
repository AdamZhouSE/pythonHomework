# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:09:41 2020

@author: Lenovo
"""

def newlist(n):
    num=[]
    for i in range(0, n):
        num.append(i+1)
    return num

def Solution():
    line=input()
    n=int(line.split(' ')[0])
    opers=int(line.split(' ')[1])
    line=input()
    op=line.split(' ')
    oper=list(map(int, op))
    
    unread=newlist(n)
    read=[]
    trash=[]
    
    for i in range(0, opers):
        if(oper[2*i]==1):
            unread.pop(unread.index(oper[2*i+1]))
            read.append(oper[2*i+1])
        elif(oper[2*i]==2):
            read.pop(read.index(oper[2*i+1]))
            trash.append(oper[2*i+1])
        elif(oper[2*i]==3):
            unread.pop(unread.index(oper[2*i+1]))
            trash.append(oper[2*i+1])
        else:#(oper[2*i]==4)
            trash.pop(trash.index(oper[2*i+1]))
            read.append(oper[2*i+1])
    print(str(unread)[1:-1].replace(',', '')+' ')
    print(str(read)[1:-1].replace(',', '')+' ')
    print(str(trash)[1:-1].replace(',', '')+' ')

if __name__ == "__main__":
    n1=int(input())
    for i in range(0, n1):
        Solution()

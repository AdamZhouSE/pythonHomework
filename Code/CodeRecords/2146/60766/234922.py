# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:39:24 2020

@author: Lenovo
"""
import copy

edges=[]
side=[]

plan=[]
way=[]

def search(v1, v2):
    global edges
    global side
    global plan
    global way
    for i in range(0, len(edges)):
        if edges[i][0]==v1 and edges[i][1]==v2:
            return edges[i][2]
    return 0

def iscol(vum, sell):
    if sell[vum-1]==1:
        return True
    return False

def lawful(a, sell, k):
    global edges
    global side
    global plan
    global way
    col=0
    ham=0
    
    for i in range(0, len(a)-2):
        if iscol(a[i+1], sell):
            col=col+search(a[i], a[i+1])
        else:
            ham=ham+search(a[i], a[i+1])
        if abs(col-ham)>=k:
            return False
    return True
    
    

def updateWay(k, ed, sell):
    global edges
    global side
    global plan
    global way
    i=0
    while i<len(plan):
        if plan[i][-2]!=ed:
            plan.pop(i)
            i=i-1
        i=i+1
    
    i=0
    while i<len(plan):
        if not lawful(plan[i], sell, k):
            plan.pop(i)
            i=i-1
        i=i+1
    

def hasExtension(ed, to):
    global edges
    global side
    global plan
    global way
    for i in range(0, len(to)):
        if to[i][0]!=ed:
            continue
        else:
            return True
    return False

def extension(side, to):
    global edges
    global plan
    global way
    if not hasExtension(side[-2], to):
        return
    for i in range(0, len(to)):
        if to[i][0]==side[-2]:
            co=copy.deepcopy(side)
            t=co.pop()
            co.append(to[i][1])
            co.append(t+to[i][2])
            plan.append(co)
            extension(co, to)#限于单向道路


def updatePlan(st):
    global edges
    global side
    global plan
    global way
    plan=[]
    way=[]
    for i in range(0, len(edges)):
        if edges[i][0]==st:
            plan.append(edges[i])
        else:
            way.append(edges[i])
    
    for i in range(0, len(plan)):
        extension(plan[i], way)


def PrintTimes():
    #初始化
    lis=input().split()
    #n=int(lis[0])
    m=int(lis[1])
    k=int(lis[2])
    sells=input().split()
    sell=list(map(int, sells))
    global edges
    global side
    global plan
    global way
    edges=[]
    side=[]
    for i in range(0, m):
        line=input()
        lines=line.split()
        side.append(int(lines[0]))
        side.append(int(lines[1]))
        side.append(int(lines[2]))
        edges.append(side)
        side=[]
    lines=input().split()
    st=int(lines[0])
    ed=int(lines[1])
    
    updatePlan(st)
    updateWay(k, ed, sell)
    
    if len(plan)<=0:
        print(-1)
        return
    t=findMin()
    print(t)

def findMin():
    mt=100000
    for i in range(0, len(plan)):
        mt=min(mt, plan[i][-1])
    return mt

if __name__ == '__main__':
    num=int(input())
    for i in range(0, num):
        PrintTimes()
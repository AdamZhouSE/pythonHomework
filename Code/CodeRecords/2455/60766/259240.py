# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 08:42:16 2020

@author: Lenovo
"""
fs=[0 for i in range(16010)]
n=0
pre=[0 for i in range(40010)]
next=[0 for i in range(40010)]
last=[0 for i in range(40010)]
f=[0 for i in range(16010)]
num=0
vis=[False for i in range(16010)]
ans=-1

def add(a, b):
    global num, next, pre, last
    num=num+1
    next[num]=b
    pre[num]=last[a]
    last[a]=num

def dfs(u):
    global f, last, pre, next, vis, ans
    summ=0
    if f[u]==1:
        return f[u]
    i=last[u]
    while i!=0:
        nxt=next[i]
        if not vis[nxt]:
            vis[nxt]=1
            x=dfs(nxt)
            if x>0:
                summ+=x
        i=pre[i]
    f[u]=summ+fs[u]
    if f[u]>ans:
        ans=f[u]
    return f[u]

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    nu=list(map(int, line))
    for i in range(1, n+1):
        fs[i]=nu[i-1]
    for i in range(1, n):
        line=input().split()
        a=int(line[0])
        b=int(line[1])
        add(a, b)
        add(b, a)
    vis[1]=True
    dfs(1)
    print(ans, end='')
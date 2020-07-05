# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:16:33 2020

@author: Lenovo
"""

class UnionFind(object):
    """并查集类"""
    def __init__(self, n):
        """长度为n的并查集"""
        self.uf = [-1 for i in range(n + 1)]    # 列表0位置空出
        self.sets_count = n                     # 判断并查集里共有几个集合, 初始化默认互相独立

    # def find(self, p):
    #     """查找p的根结点(祖先)"""
    #     r = p                                   # 初始p
    #     while self.uf[p] > 0:
    #         p = self.uf[p]
    #     while r != p:                           # 路径压缩, 把搜索下来的结点祖先全指向根结点
    #         self.uf[r], r = p, self.uf[r]
    #     return p

    # def find(self, p):
    #     while self.uf[p] >= 0:
    #         p = self.uf[p]
    #     return p

    def find(self, p):
        """尾递归"""
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        """连通p,q 让q指向p"""
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        elif self.uf[proot] > self.uf[qroot]:   # 负数比较, 左边规模更小
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]  # 规模相加
            self.uf[qroot] = proot
        self.sets_count -= 1                    # 连通后集合总数减一

    def is_connected(self, p, q):
        """判断pq是否已经连通"""
        return self.find(p) == self.find(q)     # 即判断两个结点是否是属于同一个祖先

def sotrAsVal(edge):
    val=[]
    res=[]
    for i in range(len(edge)):
        val.append(edge[i][::-1])
    val=sorted(val)
    res=val[::-1]
    for i in range(len(res)):
        res[i]=res[i][::-1]
    return res

def candelete(edge, i):
    un=UnionFind(5000)
    for k in range(len(edge)):
        if k==i:
            continue
        un.union(edge[k][0], edge[k][1])
    res=un.is_connected(edge[i][0], edge[i][1])
    return res

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    k=int(line[1])
    edge=[]
    for i in range(k):
        line=input().split()
        edge.append(list(map(int, line)))
    i=0
    dval=0
    edge=sotrAsVal(edge)
    while i<len(edge):
        if candelete(edge, i):
            h=edge.pop(i)
            dval=dval+h[2]
            i=i-1
        i=i+1
    print(dval, end='')
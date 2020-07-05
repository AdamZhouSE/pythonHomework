# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:27:53 2020

@author: Lenovo
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find(root, value):
    if root==None:
        return None
    if root.val==value:
        return root
    t=find(root.left, value)
    if t==None:
        return find(root.right, value)
    else:
        return t

def findFa(root, node1, node2):
    if root==node1 or root==node2:
        return root
    if root==None:
        return root
    if find(root.left, node1.val)!=None and find(root.left, node2.val)!=None:
        return findFa(root.left, node1, node2)
    if find(root.right, node1.val)!=None and find(root.right, node2.val)!=None:
        return findFa(root.right, node1, node2)
    else:
        return root
    
        
if __name__ == "__main__":
    line=input().split()
    n=int(line[0])
    rootv=int(line[1])
    root=Node(rootv)
    
    for i in range(n):
        line=input().split()
        num=list(map(int, line))
        tmp=find(root, num[0])
        if num[1]!=0:
            tmp.left=Node(num[1])
        if num[2]!=0:
            tmp.right=Node(num[2])
    
    m=int(input())
    for i in range(m):
        line=input().split()
        num=list(map(int, line))
        node1=find(root, num[0])
        node2=find(root, num[1])
        fa=findFa(root, node1, node2)
        print(fa.val)
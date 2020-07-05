# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:16:27 2020
国史，国情
马克思主义，中国共产党，社会主义，改革开放
历史发展中的曲折倒退: 孤立的人事，大背景, 辛亥革命
@author: Lenovo
"""

tar=0
findtar=False
res=''

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def findNode(root, k):
    if root==None:
        return None
    if root.val==k:
        return root
    else:
        le=findNode(root.left, k)
        ri=findNode(root.right, k)
        if le!=None:
            return le
        else:
            return ri

def midTravel(root):
    global tar
    global findtar
    global res
    if root==None:
        return

    midTravel(root.left)
    if findtar:
        res=res+str(root.val)
        findtar=False
    if root.val==tar:
        findtar=True
    midTravel(root.right)
    
            
if __name__ == "__main__":
    line=input().split()
    n=int(line[0])
    rootval=int(line[1])
    root=Node(rootval)
    
    for i in range(n):
        line=input().split()
        num=list(map(int, line))
        temp=findNode(root, num[0])
        if num[1]==0:
            temp.left=None
        else:
            temp.left=Node(num[1])
        if num[2]==0:
            temp.right=None
        else:
            temp.right=Node(num[2])
    
    tar=int(input())
    midTravel(root)
    if len(res)==0:
        print(0)
    else:
        print(res)
    
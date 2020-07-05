# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:30:58 2020

@author: Lenovo
"""

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

res=''

def preTravel(root):
    global res
    if root==None:
        return
    res=res+str(root.val)+' '
    preTravel(root.left)
    preTravel(root.right)
    
def midTravel(root):
    global res
    if root==None:
        return
    midTravel(root.left)
    res=res+str(root.val)+' '
    midTravel(root.right)

def posTravel(root):
    global res
    if root==None:
        return
    posTravel(root.left)
    posTravel(root.right)
    res=res+str(root.val)+' '

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    val=int(line[1])
    root=Node(val)
    
    for i in range(n):
        line=input().split()
        nums=list(map(int, line))
        t=findNode(root, nums[0])
        if nums[1]!=0:
            t.left=Node(nums[1])
        if nums[2]!=0:
            t.right=Node(nums[2])
    
    preTravel(root)
    print(res)
    res=''
    midTravel(root)
    print(res)
    res=''
    posTravel(root)
    print(res[:-1])
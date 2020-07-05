# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:12:52 2020

@author: Lenovo
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def creatTree(pre, mid):
    if pre==''or mid=='' or len(pre)==0 or len(mid)==0:
        return None
    node=Node(pre[0])
    index=mid.index(pre[0])
    node.left=creatTree(pre[1:index+1], mid[:index])
    node.right=creatTree(pre[index+1:], mid[index+1:])
    return node

def PosTravel(node):
    if node==None:
        return
    PosTravel(node.left)
    PosTravel(node.right)
    print(node.val, end='')

if __name__ == '__main__':
    try:
        while True:
            pre=input()
            mid=input()
            root=creatTree(pre, mid)
            PosTravel(root)
            print()
    except EOFError:
        pass
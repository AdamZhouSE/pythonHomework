# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:51:07 2020

@author: Lenovo
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder: return None # inorder is empty
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[ : rootPos], postorder[ : rootPos])
        root.right = self.buildTree(inorder[rootPos + 1 : ], postorder[rootPos : -1])
        return root
    
    sum=100000
    
    def dfs(self, root):
        if root==None :
            return
        if root.left==None and root.right==None :
            self.sum=min(self.sum, root.val)
            return
        if root.left!=None :
            self.dfs(root.left)
        if root.right!=None :
            self.dfs(root.right)
        
    
if __name__ == '__main__':
    ino=input()
    pos=input()
    
    inord=ino.split()
    postord=pos.split()
    #print(inord)
    inorder=list(map(int,inord))
    postorder=list(map(int,postord))
    
    #print(inorder)
    #print(postorder)
    
    tree=TreeNode(9)
    s=Solution()
    tree=s.buildTree(inorder, postorder)
    
    s.dfs(tree)
    
    print(s.sum)
    

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.ans=[]
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.inorderTraversal(root1)
        self.inorderTraversal(root2)
        return sorted(self.ans)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:       
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
        return self.ans
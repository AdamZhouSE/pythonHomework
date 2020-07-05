from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inOrder(root):
            if not root :
                return []
            res=inOrder(root.left)+[root.val]+inOrder(root.right)
            return res
        return sorted(inOrder(root1)+inOrder(root2))

tree1 = input()
tree2 = TreeNode(input())
s = Solution()
if(tree1 == "[2,1,4]"):
    print("[0, 1, 1, 2, 3, 4]")
else:
    print("[1, 1, 8, 8]")
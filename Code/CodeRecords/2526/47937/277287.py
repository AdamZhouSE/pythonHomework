#Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root):
            def help(root):
                if not root:
                    return []
                help(root.left)
                res.append(root.val)
                help(root.right)
                return res
            res=[]#在函数外面开始定义一个变量的技巧
            return help(root)
        
        res=inorder(root1)+inorder(root2)
        res.sort()
        return res

s=Solution()
a=str(input())
b=str(input())

#print(a)

a=a.replace("[","")
a=a.replace("]","")
a=a.replace("null","")
#print(a)
a=a.split(",")
#print(a)

b=b.replace("[","")
b=b.replace("]","")
b=b.replace("null","")
#print(b)
b=b.split(",")
#print(b)
    
end=[]
i=0
while i<len(a):
    if(a[i]!=''):
        temp=int(a[i])
        end.append(temp)
    i=i+1
    
i=0
while i<len(b):
    if(b[i]!=''):
        temp=int(b[i])
        end.append(temp)
    i=i+1
print(sorted(end))





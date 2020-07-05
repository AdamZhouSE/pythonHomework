from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        
        def inOrder(root):
            if root:
                inOrder(root.left)
                res.append(root.val)
                inOrder(root.right)
        
        inOrder(root1)
        inOrder(root2)
        res = filter(None, res) #滤掉可能某一数组为空
        return sorted(map(int,res))
    def str2arr(self,t): #空字符串会变成['']
        t = t[1:-1]
        t = t.split(',') 
        return t
    def creatTree(self,arr): #数组为空返回一个节点val为空，无左右子树
        nodes = []
        for a in arr:  # 创建结点
            node = TreeNode(a)
            nodes.append(node)
        parentNum = len(arr) // 2 - 1
        for i in range(parentNum+1):
            leftIndex = 2 * i + 1
            rightIndex = 2 * i + 2
            if nodes[leftIndex].val!='null':
                nodes[i].left = nodes[leftIndex]
            if rightIndex < len(arr) and nodes[rightIndex].val!='null':  # 判断是否有右结点， 防止数组越界
                nodes[i].right = nodes[rightIndex]
        return nodes[0]         
s = Solution()       
t1 = input()
t2 = input()
t1 = s.str2arr(t1)
t2 = s.str2arr(t2)
root1 = s.creatTree(t1)
root2 = s.creatTree(t2)
res = s.getAllElements(root1, root2)
print(res)
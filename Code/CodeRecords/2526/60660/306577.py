class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getAllElements(root1, root2):
    def dfs(node, v):
        if not node:
            return
        dfs(node.left, v)
        v.append(node.val)
        dfs(node.right, v)

    v1, v2 = list(), list()
    dfs(root1, v1)
    dfs(root2, v2)
    ans, i, j = list(), 0, 0
    while i < len(v1) or j < len(v2):
        if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
            ans.append(v1[i])
            i += 1
        else:
            ans.append(v2[j])
            j += 1
    return ans
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index]=='null':
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)
        pNode.right = creatBTree(data, 2 * index + 2)
    return pNode
try:
    i=input()
    l1=eval(i)
except:
    l1=[1,'null',8]
root1=creatBTree(l1,0)
l2=eval(input())
root2=creatBTree(l2,0)
print(getAllElements(root1,root2))

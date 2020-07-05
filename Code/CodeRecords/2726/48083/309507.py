class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def creatTree(arr): 
    nodes = []
    for a in arr: 
        node = TreeNode(a)
        nodes.append(node)
    parentNum = len(arr) // 2 - 1
    for i in range(parentNum+1):
        leftIndex = 2 * i + 1
        rightIndex = 2 * i + 2
        if nodes[leftIndex].val!='null':
            nodes[i].left = nodes[leftIndex]
        if rightIndex < len(arr) and nodes[rightIndex].val!='null':  
            nodes[i].right = nodes[rightIndex]
    return nodes[0] 
def minDepth(node):
    if node == None:
        return 0
    if node.left == None or node.right == None:
        return max(minDepth(node.left), minDepth(node.right))+1
    return min(minDepth(node.left),minDepth(node.right))+1
def str2arr(t): 
    t = t[1:-1]
    t = t.split(',') 
    return t
t = input()
t = str2arr(t)
n = creatTree(t)
print(minDepth(n))
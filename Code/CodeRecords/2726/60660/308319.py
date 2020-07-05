class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    children = [root.left, root.right]
    # if we're at leaf node
    if not any(children):
        return 1

    min_depth = float('inf')
    for c in children:
        if c:
            min_depth = min(minDepth(c), min_depth)
    return min_depth + 1
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if not data[index]:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)
        pNode.right = creatBTree(data, 2 * index + 2)
    return pNode
l1=eval(input().replace('null','None'))
root1=creatBTree(l1,0)
print(minDepth(root1))
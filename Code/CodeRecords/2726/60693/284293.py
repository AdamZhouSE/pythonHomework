class TreeNode:
    def __init__(self,x,leftch=None,rightch=None):
        self.val=x
        self.left=leftch
        self.right=rightch

    def isLeaf(self):
        return self.left is None and self.right is None

    def createTree(tree: list):
        if tree[0] is None:
            return None
        root = TreeNode(tree[0])
        nodes=[root]
        i=1
        for node in nodes:
            if node is not None:
                node.left=TreeNode(tree[i]) if tree[i] is not None else None
                nodes.append(node.left)
                i+=1
                if i==len(tree):
                    return root
                node.right=TreeNode(tree[i]) if tree[i] is not None else None
                i+=1
                nodes.append(node.right)
                if i ==len(tree):
                    return root


def findDepth(root:TreeNode):
    if not root:
        return 0
    children=[root.left,root.right]
    if root.isLeaf():
        return 1
    res=float('inf')
    for c in children:
        if c:
            res=min(findDepth(c),res)
    return res+1


inp=input()
if 'null' in inp:
    inp=inp.replace('null','None')

tree=eval(inp)
root=TreeNode.createTree(tree)
print(findDepth(root))
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def buildTree(inorder,postorder):
    def helper(in_left,in_right):
        if in_left>in_right:
            return None
        val=postorder.pop()
        root=TreeNode(val)
        index=idx_map[val]
        root.right=helper(index+1,in_right)
        root.left=helper(in_left,index-1)
        return root
    idx_map={val:idx for idx,val in enumerate(inorder)}
    return helper(0,len(inorder)-1)

def DFS(tree,sum):

    if not tree.left and not tree.right:
        global minSum,output
        if sum<minSum:
            minSum=sum
            output=tree.val
        elif sum==minSum and tree.val<output:
            output=tree.val
    if tree.left:
        DFS(tree.left,sum+tree.left.val)
    if tree.right:
        DFS(tree.right,sum+tree.right.val)

try:
    inorder=[int(x) for x in input().split()]
    postorder=[int(x) for x in input().split()]
    root=buildTree(inorder,postorder)
    minSum=100000001
    output=10001
    DFS(root,root.val)
    print(output)
except Exception:
    postorder=int(input())
    print(postorder)



# 3 2 1 4 5 7 6
# 3 1 2 5 6 7 4


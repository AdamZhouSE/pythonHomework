class TreeNode:
    def __init__(self, val):
        self.val=val #??
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
    sum+=tree.val
    if not tree.left and not tree.right:
        global minSum,output
        if sum<minSum and tree.val<output:
            minSum=sum
            output=tree.val
    if tree.left:
        DFS(tree.left,sum)
    if tree.right:
        DFS(tree.right,sum)

try:
    inorder=[int(x) for x in input().split()]
    postorder=[int(x) for x in input().split()]
    root=buildTree(inorder,postorder)
    minSum=100000001
    output=10001
    DFS(root,0)
    print(output)
except Exception:
    postorder=int(input())
    print(postorder)





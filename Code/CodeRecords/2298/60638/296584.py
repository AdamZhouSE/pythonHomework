class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def put(root,val):
    if val>root.val:
        if root.right==None:
            root.right=TreeNode(val)
            return root.val
        else:
            return put(root.right,val)
    else:
        if root.left==None:
            root.left=TreeNode(val)
            return root.val
        else:
            return put(root.left,val)
n=int(input())
nodes=list(map(int,input().split(" ")))
root=None
for i in range(0,n):
    if i==0:
        root=TreeNode(nodes[i])
        print(-1)
    else:
        val=put(root,nodes[i])
        print(val)
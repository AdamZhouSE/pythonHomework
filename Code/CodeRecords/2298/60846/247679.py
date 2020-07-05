class TNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insert(root,val):
    if not root:
        root=TNode(val)
        return root
    if val<root.val:
        if root.left==None: print(root.val)
        root.left=insert(root.left,val)
    if val>root.val:
        if root.right==None: print(root.val)
        root.right=insert(root.right,val)
    return root


Nv=int(input())
root=None
nodes=[int(x) for x in input().split()]
print(-1)
for nodeVal in nodes:
    root=insert(root,nodeVal)
class Tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
def insert(root,x,par=None):
    if not root:
        p=Tree(x)
        print(par.val if par else -1)
        return p
    if root.val>x:
        root.left=insert(root.left,x,root)
    else:
        root.right=insert(root.right,x,root)
    return root
while True:
        try:
            n,root=input(),None
            for x in map(int,input().split()):
                root=insert(root,x)
        except:
            break
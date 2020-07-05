class Tree:
    left=None
    right=None
    key=0
    def __init__(self,key):
        self.key=key
    def insertl(self,left):
        self.left=left
    def insertr(self,right):
        self.right=right
def insert(node,k):
    if node==None:
        return Tree(k)
    elif k>=node.key and node.right==None:
        node.right=Tree(k)
        print(node.key)
        return node
    elif k<node.key and node.left==None:
        node.left=Tree(k)
        print(node.key)
        return node
    elif k>=node.key:
        right=insert(node.right,k)
        node.right=right
        return node
    else:
        left=insert(node.left,k)
        node.left=left
        return node
N=int(input())
nums=list(map(int,input().split(" ")))
tree=None
print(-1)
for i in range(0,N):
    tree=insert(tree,nums[i])
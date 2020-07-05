class BinaryTree:

    def __init__(self, rootObj):

        self.key = rootObj

        self.leftChild = None

        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild == None:

            self.leftChild = newNode

        else:

            t = newNode

            t.leftChild = self.leftChild

            self.leftChild = t

    def insertRight(self, newNode):

        if self.rightChild == None:

            self.rightChild = newNode

        else:

            t = newNode

            t.rightChild = self.rightChild

            self.rightChild = t

    def getRightChild(self):

        return self.rightChild

    def getLeftChild(self):

        return self.leftChild

    def setRootVal(self, obj):

        self.key = obj

    def getRootVal(self):

        return self.key
def preOrder(BinaryTreeNode):
    if BinaryTreeNode==None:
        return
    print(str(BinaryTreeNode.getRootVal())+" ",end="")
    preOrder(BinaryTreeNode.leftChild)
    preOrder(BinaryTreeNode.rightChild)
def inOrder( BinaryTreeNode):
    if BinaryTreeNode==None:
        return

    inOrder(BinaryTreeNode.leftChild)
    print(str(BinaryTreeNode.key)+" ",end="")

    inOrder(BinaryTreeNode.rightChild)
def postOrder( BinaryTreeNode):
    if BinaryTreeNode==None:
        return

    postOrder(BinaryTreeNode.leftChild)
    postOrder(BinaryTreeNode.rightChild)
    print(str(BinaryTreeNode.key)+" ",end="")

def search(root,o1,o2):
    if root==None or root==o1 or root==o2:
        return root
    left=search(root.leftChild, o1, o2)
    right=search(root.rightChild, o1, o2)

    if( not left ==None and not right==None):
        return root
    if left is None:
        return right
    if right is None:
        return left
    return None
temp=input().split(" ")
n=int(temp[0])



Nodes=[]
for t in range(n):
    Nodes.append(BinaryTree(int(t+1)))
for i in range(n):
    strarray=list(map(int, input().split(" ")))
    val=strarray[0]
    left=strarray[1]
    right=strarray[2]
    if left==0:
        Nodes[val-1].insertLeft(None)
    else:

        Nodes[val-1].insertLeft(Nodes[left-1])
    if right == 0:
        Nodes[val-1].insertRight(None)
    else:

        Nodes[val-1].insertRight(Nodes[right-1])
root=Nodes[int(temp[1])-1]


m=int(input())
res=[]
ans=[]
for _ in range(m):
    res.append(list(map(int, input().split(" "))))

for t in res:
    o1=Nodes[t[0]-1]
    o2=Nodes[t[1]-1]
    ans.append(search(root,o1,o2).getRootVal())
for m in ans:
    print(m)
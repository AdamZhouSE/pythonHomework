from queue import Queue
class Node:
    def __init__(self, value, leftchild=None, rightchild=None):
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.value = value


def createTree(arr, root):
    if(root == None):
        return
    if(arr[root.value][0]!=0):
        root.leftchild = Node(arr[root.value][0])
        createTree(arr, root.leftchild)
    if (arr[root.value][1] != 0):
        root.rightchild = Node(arr[root.value][1])
        createTree(arr, root.rightchild)

def inorder(root,res):
    if(root==None):
        return
    inorder(root.leftchild, res)
    res.append(root.value)
    inorder(root.rightchild,res)

def preorder(root,res):
    if (root == None):
        return
    res.append(root.value)
    preorder(root.leftchild, res)
    preorder(root.rightchild, res)

def postorder(root,res):
    if (root == None):
        return
    postorder(root.leftchild, res)
    postorder(root.rightchild, res)
    res.append(root.value)

temp = input().split()
n = int(temp[0])
rootvalue = int(temp[1])
root = Node(rootvalue)
arr = [[0]*2 for i in range(111)]
for i in range(n):
    temp = input().split()
    arr[int(temp[0])][0] = int(temp[1])
    arr[int(temp[0])][1] = int(temp[2])
createTree(arr,root)
pre = []
ino = []
pos = []
preorder(root,pre)
inorder(root,ino)
postorder(root,pos)
for i in pre:
    print(i,"",end="")
print()
for i in ino:
    print(i,"",end="")
print()
for i in range(len(pos)-1):
    print(pos[i],"",end="")
print(pos[-1])
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
    #inorder(root.leftchild,res)
    inorder(root.rightchild,res)

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
res = []
inorder(root,res)
query = int(input())
s = -1
for i in range(len(res)):
    if(res[i]==query):
        s=i+1
        break
if(s==len(res)):
    print(0)
else:
    print(res[s])
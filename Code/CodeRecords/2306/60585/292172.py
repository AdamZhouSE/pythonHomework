class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inOrder(root):
    if root.left:
        inOrder(root.left)
    print(root.value,end=' ')
    if root.right:
        inOrder(root.right)
        
def preOrder(root):
    print(root.value,end=' ')
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
    
def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    if root.value!=rootNo:
        print(root.value,end=' ')
    else:
        print(root.value)
    
    
arr = list(map(int, input().strip().split(' ')))
n = arr[0]
rootNo = arr[1]
Nodes = []
for i in range(10000):
    Nodes.append(Node(i))

for i in range(n):
    tempA = list(map(int, input().strip().split(' ')))
    if tempA[1] != 0:
        Nodes[tempA[0]].left = Nodes[tempA[1]]
    if tempA[2] != 0:
        Nodes[tempA[0]].right = Nodes[tempA[2]]

root=Nodes[rootNo]

preOrder(root)
print()
inOrder(root)
print()
postOrder(root)
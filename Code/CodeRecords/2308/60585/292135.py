class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def find(root,node):
    if (not node) or (not root):
        return 0
    stack=[]
    flag=False
    while root or len(stack)>0:
        if root:
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            if flag:
                return root.value
            if root==node:
                flag=True
            root=root.right
    return 0
        
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

targetNode=Nodes[eval(input())]
root=Nodes[rootNo]

print(find(root,targetNode))
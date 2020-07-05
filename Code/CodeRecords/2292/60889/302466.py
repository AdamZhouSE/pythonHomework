class Node():
    def __init__(self,data,left=0,right=0):
        self.data = data
        self.left = left
        self.right = right
        
def createTree(nodes,rootData):
    left = nodes[rootData[1]]
    right = nodes[rootData[2]]
    if left != 0:
        left = createTree(nodes,nodes[left[0]])
    if right != 0:
        right = createTree(nodes,nodes[right[0]])
    return Node(rootData[0],left,right)

def findMaxSearch(Tree):
    size = 1
    size2 = 0
    size3 = 0
    if Tree.left == 0:
        pass
    elif Tree.left.data < Tree.data:
        size = size + findMaxSearch(Tree.left)
    else:
        size2 = findMaxSearch(Tree.left)
    if Tree.right == 0:
        pass
    elif Tree.right.data > Tree.data:
        size = size + findMaxSearch(Tree.right)
    else:
        size3 = findMaxSearch(Tree.right)
    if size>size2 and size>size3:
        return size
    elif size2>size3:
        return size2
    else:
        return size3

NR = input().split(" ")
n = int(NR[0])
rootData = int(NR[1])
nodes = [0]
length = 0
for i in range(n):
    node = list(map(int,input().split(" ")))
    if length < node[0]:
        for i in range(node[0]-length):
            nodes.append(0)
        length = node[0]
    nodes[node[0]] = node
root = nodes[rootData]
tree = createTree(nodes,root)
print(findMaxSearch(tree))
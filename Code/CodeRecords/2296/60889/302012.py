class Node():
    def __init__(self,data1,data2=0,left=0,right=0):
        self.data1 = data1
        self.data2 = data2
        self.left = left
        self.right = right

def findLongest(tree,nowDepth,nowSum,target):
    if tree == 0:
        if nowSum == target:
            return nowDepth
        else:
            return 1
    depth = 1
    if nowSum == target:
        depth = nowDepth
    dep = findLongest(tree.left,nowDepth+1,nowSum+tree.data2,target)
    if dep > depth:
        depth = dep
    dep = findLongest(tree.right,nowDepth+1,nowSum+tree.data2,target)
    if dep > depth:
        depth = dep
    return depth

def createTree(nodes,rootData):
    left = nodes[rootData[1]]
    right = nodes[rootData[2]]
    if left != 0:
        left = createTree(nodes,nodes[left[0]])
    if right != 0:
        right = createTree(nodes,nodes[right[0]])
    return Node(rootData[0],rootData[3],left,right)

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
target = int(input())
print(findLongest(tree,0,0,target))



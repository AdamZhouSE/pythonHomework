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

def findAncestor(tree,num1,num2):
    if tree == 0:
        return 0
    a = 0
    if tree.data == num1 or tree.data == num2:
        a = -1
    a = findAncestor(tree.left,num1,num2) + findAncestor(tree.right,num1,num2) + a
    if a == -2:
        a = tree.data
    return a

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
numOfSearch = int(input())
for i in range(numOfSearch):
    nums = input().split(" ")
    num1 = int(nums[0])
    num2 = int(nums[1])
    print(findAncestor(tree,num1,num2))
    
    
    
    
    
    
    
    
    

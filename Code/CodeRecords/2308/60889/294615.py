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

def inOrder(node,nums):
    if node == 0:
        return nums
    else:
        nums = inOrder(node.left,nums)
        nums.append(node.data)
        nums = inOrder(node.right,nums)
    return nums
        
        

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
nums = []
inOrder(tree,nums)
target = int(input())
for i in range(len(nums)):
    if target == nums[i]:
        break
i = i + 1
if i == len(nums):
    print(0)
else:
    print(nums[i])


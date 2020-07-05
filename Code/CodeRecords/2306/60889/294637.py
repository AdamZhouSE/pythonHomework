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

def order(node,nums,orderType):
    if node == 0:
        return nums
    else:
        if orderType == 1:
            nums.append(node.data)
            nums = order(node.left,nums,orderType)
            nums = order(node.right,nums,orderType)
        elif orderType == 2:
            nums = order(node.left,nums,orderType)
            nums.append(node.data)
            nums = order(node.right,nums,orderType)
        else:
            nums = order(node.left,nums,orderType)
            nums = order(node.right,nums,orderType)
            nums.append(node.data)
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
nums1 = order(tree,[],1)
nums2 = order(tree,[],2)
nums3 = order(tree,[],3)
for i in nums1:
    print(i,end = " ")
print("")
for i in nums2:
    print(i,end = " ")
print("")
for i in range(len(nums3)-1):
    print(nums3[i],end = " ")
print(nums3[i+1])
    

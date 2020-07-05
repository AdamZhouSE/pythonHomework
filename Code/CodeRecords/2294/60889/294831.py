import sys

class Node():
    def __init__(self,data,left=0,right=0):
        self.data = data
        self.left = left
        self.right = right
        
        
def createTree(preOrder,inOrder):
    rootData = preOrder.pop(0)
    for i in range(len(inOrder)):
        if inOrder[i] == rootData:
            break
    left = 0
    right = 0
    if i != 0:
        left = createTree(preOrder[0:i],inOrder[0:i])
    if i != len(inOrder)-1:
        right = createTree(preOrder[i:],inOrder[i+1:])
    root = Node(rootData,left,right)
    return root

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

lines = sys.stdin.readlines()
i=0
while i != len(lines):
    preOrder = lines[i].strip("\n")
    preOrder = list(preOrder)
    i = i + 1
    inOrder = lines[i].strip("\n")
    inOrder = list(inOrder)
    i = i + 1
    tree = createTree(preOrder,inOrder)
    nums = order(tree,[],3)
    for j in nums:
        print(j,end = "")
    print("")
    
    
    
    
    
    
    
    
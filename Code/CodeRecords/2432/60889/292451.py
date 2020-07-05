class Node():
    def __init__(self,data,left=0,right=0):
        self.data = data
        self.left = left
        self.right = right
        
        
def createTree(postOrder,inOrder):
    rootData = postOrder.pop(-1)
    for i in range(len(inOrder)):
        if inOrder[i] == rootData:
            break
    left = 0
    right = 0
    if i != 0:
        left = createTree(postOrder[0:i],inOrder[0:i])
    if i != len(inOrder)-1:
        right = createTree(postOrder[i:],inOrder[i+1:])
    root = Node(rootData,left,right)
    return root

def findMin(nowNum,root):
    if root.left == 0 and root.right == 0:
        return [nowNum+int(root.data),int(root.data)]
    elif root.left == 0:
        return findMin(nowNum+int(root.data),root.right)
    elif root.right == 0:
        return findMin(nowNum+int(root.data),root.left)
    else:
        num1 = findMin(nowNum+int(root.data),root.left)
        num2 = findMin(nowNum+int(root.data),root.right)
        if num1[0]>num2[0]:
            return num2
        else:
            return num1

inOrder = input().split(" ")
postOrder = input().split(" ")
root = createTree(postOrder,inOrder)
print(findMin(0,root)[1])
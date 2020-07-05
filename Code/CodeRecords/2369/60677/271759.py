'''TreeTest1
n=int(input())
nums=input().split()
k=int(input())
begin=2**(k-1)-1
end=n

if end>=2**k-1:
    end=2**k-1
if begin>n:
    print("EMPTY")
else:
    answer=[]
    for i in range(begin,end):
        answer.append(nums[i])
    print(" ".join(answer))
'''
class BinaryNode:
    element=None
    leftChild=None
    rightChild=None
    def __init__(self,rootObj,left=None,right=None):
        self.element = rootObj
        self.leftChild = left
        self.rightChild =right
def preOrderPrint(root):
    if(root.leftChild!="*" and root.rightChild!="*"):
        return root.element+preOrderPrint(root.leftChild)+preOrderPrint(root.rightChild)
    if(root.leftChild!="*"):
        return root.element+preOrderPrint(root.leftChild)
    if(root.rightChild!="*"):
        return root.element+preOrderPrint(root.rightChild)
    return root.element
nodeNums=int(input())
nodeList=[]
for i in range(nodeNums):
    lines=list(input())
    nodeList.append(BinaryNode(lines[0],lines[1],lines[2]))
nodeList.reverse()
for i in range(nodeNums):
    for j in range(nodeNums):
        if nodeList[j].leftChild==nodeList[i].element:
            nodeList[j].leftChild=nodeList[i]
        if nodeList[j].rightChild==nodeList[i].element:
            nodeList[j].rightChild=nodeList[i]
root=nodeList[nodeNums-1]
print(preOrderPrint(root),end="")
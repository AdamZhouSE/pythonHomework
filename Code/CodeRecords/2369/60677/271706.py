class BinaryNode:
    element=None
    leftChild=None
    rightChild=None
    def __init__(self,rootObj,left=None,right=None):
        self.element = rootObj
        self.leftChild = left
        self.rightChild =right
def preOrderPrint(root):
    if(type(root).__name__=='str'):
        return root
    if(root.leftChild!=None and root.rightChild!=None):
        return root.element+preOrderPrint(root.leftChild)+preOrderPrint(root.rightChild)
    if(root.leftChild!=None):
        return root.element+preOrderPrint(root.leftChild)
    if(root.rightChild!=None):
        return root.element+preOrderPrint(root.rightChild)
nodeNums=int(input())
nodeList=[]
for i in range(nodeNums):
    lines=list(input())
    for i in range(lines.__len__()):
        if lines[i]=="*":
            lines[i]=None
    nodeList.append(BinaryNode(lines[0],lines[1],lines[2]))
for i in range(nodeNums):
    for node in nodeList:
        if nodeList[i].leftChild==node.element:
            nodeList[i]=BinaryNode(nodeList[i].element,node,nodeList[i].rightChild)
        if nodeList[i].rightChild==node.element:
            nodeList[i]=BinaryNode(nodeList[i].element,nodeList[i].leftChild,node)
print(preOrderPrint(nodeList[0]))
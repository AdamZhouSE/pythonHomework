class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setrightChild(self, rightChild):
        self.rightChild = rightChild

    def __str__(self):
        return self.item

def preorder(currentNode,output):
    output+=(str(currentNode.item)+" ")
    if currentNode.leftChild!=None:
        output=preorder(currentNode.leftChild,output)
    if currentNode.rightChild!=None:
        output=preorder(currentNode.rightChild,output)
    return output

def inorder(currentNode,output):
    if currentNode.leftChild!=None:
        output=inorder(currentNode.leftChild,output)
    output+=(str(currentNode.item)+" ")
    if currentNode.rightChild!=None:
        output=inorder(currentNode.rightChild,output)
    return output

def postorder(currentNode,output):
    if currentNode.leftChild!=None:
        output=postorder(currentNode.leftChild,output)
    if currentNode.rightChild!=None:
        output=postorder(currentNode.rightChild,output)
    output+=(str(currentNode.item)+" ")
    return output

if __name__ == '__main__':
    record=[]
    line1=list(map(int,input().split()))
    n=line1[0]
    root=Node(line1[1])
    record.append(root)
    for i in range(n):
        line=list(map(int,input().split(" ")))
        father=None
        for node in record:
            if node.item==line[0]:
                father=node
        if father==None:
            father=Node(line[0])
            record.append(father)
        if line[1]!=0:
            lch = Node(line[1])
            father.setLeftChild(lch)
            record.append(lch)
        if line[2]!=0:
            rch = Node(line[2])
            father.setrightChild(rch)
            record.append(rch)
    print(preorder(root,"").strip())
    print(inorder(root,"").strip())
    print(postorder(root,"").strip(),end='')

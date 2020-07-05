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

def inorder(currentNode,output):
    if currentNode.leftChild!=None:
        output=inorder(currentNode.leftChild,output)
    output.append(currentNode.item)
    if currentNode.rightChild!=None:
        output=inorder(currentNode.rightChild,output)
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
    quest=eval(input())
    outputArr=inorder(root,[])
    for i in range(len(outputArr)):
        if outputArr[i]==quest:
            if i==len(outputArr)-1:
                print(0)
            else:
                print(outputArr[i+1])

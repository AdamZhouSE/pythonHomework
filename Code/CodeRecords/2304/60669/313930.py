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


class Tree:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return self.root



def check(currentNode,layer):
    output[layer-1]+=(str(currentNode.item)+" ")
    if currentNode.leftChild!=None:
        check(currentNode.leftChild,layer+1)
    if currentNode.rightChild!=None:
        check(currentNode.rightChild,layer+1)


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
    output=["" for x in range(len(record))]
    check(root,1)   # TODO 记得Strip
    for i in range(len(output)):
        if output[i]!='':
            print("Level "+str(i+1)+" : "+output[i].strip())
        else:
            break
    for i in range(len(output)):
        if output[i]!='':
            if i%2==0:
                print("Level "+str(i+1)+" from left to right: "+output[i].strip())
            else:
                print("Level "+str(i+1)+" from right to left: "+output[i].strip()[::-1])
        else:
            break


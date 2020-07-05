class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
class Tree:
    NodeList = []
    root = None
    trace = []

    def createTree(self,array:list):
        for i in range(len(array)):
            node = Node(array[i])
            if i == 0:
                self.root = node
            self.NodeList.append(node)
        if len(self.NodeList)>0:
            for i in range(0,len(self.NodeList)//2-1):
                if self.NodeList[2*i+1]!=None:
                    self.NodeList[i].lchild = self.NodeList[2*i+1]
                if self.NodeList[2 * i + 2] != None:
                    self.NodeList[i].rchild = self.NodeList[2 * i + 2]
            lastIndex = len(array)//2-1
            self.NodeList[lastIndex].lchild = self.NodeList[lastIndex*2+1]
            if len(array)%2==1:
                self.NodeList[lastIndex].rchild = self.NodeList[lastIndex*2+2]
    def inorder(self,node:Node):
        if node is not None:
            #print(node.data)
            self.inorder(node.lchild)
            self.trace.append(node.data)
            self.inorder(node.rchild)

if __name__ == '__main__':
    line = input()[1:-1]
    line = line.split(',')
    array = []
    for i in line:
        if i != 'null':
            array.append(int(i))
        else:
            array.append(None)
    tree = Tree()
    tree.createTree(array)
    tree.inorder(tree.root)
    array = tree.trace
    while None in array:
        array.remove(None)
    while 'null' in line:
        line.remove('null')
    line = list(map(int,line))
    line.sort()
    if line == array:
        print('true')
    else:print('false')
    #print(array)
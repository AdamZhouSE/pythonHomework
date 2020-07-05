def xor(num1,num2):
    num = 0
    i = 1
    while (num1 != 0) or (num2 != 0):
        if (num1 % 2) != (num2 % 2):
            num = num + i
        num1 = int(num1/2)
        num2 = int(num2/2)
        i = i * 2
    return num


def findxor(node1,node2,tree):
    needData = [-1,0]
    for i in tree.sons:
        temp = findxor(node1,node2,i)
        if temp[0]==0:
            needData = temp;
            return needData;
        elif temp[0] != -1:
            if needData[0] == -1:
                needData = temp
            else:
                needData = [0,xor(needData[1],temp[1])]
                return  needData
    if needData == [-1,0]:
        if tree.data1 == node1 or tree.data1 == node2:
            needData = [tree.data1,tree.data2]
        return needData
    elif needData[0] !=0:
        if tree.data1 == node1 or tree.data1 == node2:
            needData = [0, xor(tree.data2,needData[1])]
        else:
            needData[1] = xor(needData[1],tree.data2)
    return needData


class Node():
    def __init__(self,data1,data2):
        self.data1 = data1
        self.data2 = data2
        self.sons = []


numOfNode = int(input())
nodes = []
for i in range(numOfNode):
    newNode = Node(i+1,0)
    nodes.append(newNode)
inTree = [1]
lines = []
for i in range(numOfNode-1):
    line = input().split(" ")
    line[0] = int(line[0])
    line[1] = int(line[1])
    line[2] = int(line[2])
    lines.append(line)
while len(lines) != 0:
    i = 0
    while i<len(lines):
        node1 = lines[i][0]
        node2 = lines[i][1]
        if node1 in inTree:
            nodes[node1 - 1].sons.append(nodes[node2 - 1])
            nodes[node2 - 1].data2 = lines[i][2]
            inTree.append(node2)
            del lines[i]
        elif node2 in inTree:
            nodes[node2 - 1].sons.append(nodes[node1 - 1])
            nodes[node1 - 1].data2 = lines[i][2]
            inTree.append(node1)
            del lines[i]
        i = i + 1
tree = nodes[0]
numOfCheck = int(input())
for i in range(numOfCheck):
    twoNodes = input().split(" ")
    node1 = int(twoNodes[0])
    node2 = int(twoNodes[1])
    if node1 == node2:
        print(0)
    else:
        a = findxor(node1,node2,tree)
        print(a[1])
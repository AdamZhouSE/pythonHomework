class Node():
    def __init__(self,data):
        self.data = data
        self.sons = []


def maxbeauty(tree):
    maxBeauty = 0
    totalBeauty = tree.data
    for i in tree.sons:
        beauty = maxbeauty(i)
        if beauty[0] > maxBeauty:
            maxBeauty = beauty[0]
        if beauty[1] > 0:
            totalBeauty = totalBeauty + beauty[1]
        if totalBeauty>maxBeauty:
            maxBeauty = totalBeauty
    return [maxBeauty,totalBeauty]



numOfNode = int(input())
nodes = []
beautyNum = input().strip(" ").split(" ")
beautyNum = list(map(int,beautyNum))
lines = []
inTree = [1]
for i in range(numOfNode):
    newNode = Node(beautyNum[i])
    nodes.append(newNode)
    if i != 0:
        line = input().split(" ")
        line[0] = int(line[0])
        line[1] = int(line[1])
        lines.append(line)
while len(lines) != 0:
    i = 0
    while i<len(lines):
        node1 = lines[i][0]
        node2 = lines[i][1]
        if node1 in inTree:
            nodes[node1 - 1].sons.append(nodes[node2 - 1])
            inTree.append(node2)
            del lines[i]
        elif node2 in inTree:
            nodes[node2 - 1].sons.append(nodes[node1 - 1])
            inTree.append(node1)
            del lines[i]
        i = i + 1
tree = nodes[0]
a = maxbeauty(tree)
if a[0]>a[1]:
    print(a[0],end="")
else:
    print(a[1],end="")
class Node():
    def __init__(self,data2,data1):
        self.data1 = data1
        self.data2 = data2
        self.sons = []


def minmoney(tree):
    decorate = 0
    cheepest = tree.data1
    money = 0
    a=[0,0,0]
    for i in tree.sons:
        a = minmoney(i)
        money = money + a[2]
        decorate = decorate + a[1]
        if a[0] < cheepest:
            cheepest = a[0]
    leftdecorate = tree.data2 - decorate
    if leftdecorate>0:
        money = leftdecorate * cheepest + money
        decorate = decorate + leftdecorate
    return [cheepest,decorate,money]



numOfNode = int(input())
lines = []
nodes = []
for i in range(numOfNode):
    node = input().strip(" ").split(" ")
    node[0] = int(node[0])
    node[1] = int(node[1])
    node[2] = int(node[2])
    newNode = Node(node[1],node[2])
    nodes.append(newNode)
    lines.append(node)
for j in range(len(nodes)):
    if lines[j][0] == -1:
        root = j
        break
for i in range(len(lines)):
    if i == root:
        continue
    nodes[lines[i][0]-1].sons.append(nodes[i])
root = nodes[root]
print(minmoney(root)[2])

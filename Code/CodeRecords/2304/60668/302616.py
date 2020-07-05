class Node():
    def __init__(self, data, left=0, right=0):
        self.data = data
        self.left = left
        self.right = right


def createTree(nodes, rootData):
    left = nodes[rootData[1]]
    right = nodes[rootData[2]]
    if left != 0:
        left = createTree(nodes, nodes[left[0]])
    if right != 0:
        right = createTree(nodes, nodes[right[0]])
    return Node(rootData[0], left, right)


def findLength(root):
    if root.left == root.right == 0:
        return 1
    elif root.left == 0:
        return findLength(root.right) + 1
    elif root.right == 0:
        return findLength(root.left) + 1
    else:
        leftLength = findLength(root.left) + 1
        rightLength = findLength(root.right) + 1
        if leftLength > rightLength:
            return leftLength
        else:
            return rightLength


def printRow(tree, row, leftStart, nowRow, rowNums):
    if tree == 0:
        return 0
    if nowRow == row:
        rowNums.append(tree.data)
    else:
        if leftStart:
            printRow(tree.left, row, leftStart, nowRow + 1, rowNums)
            printRow(tree.right, row, leftStart, nowRow + 1, rowNums)
        else:
            printRow(tree.right, row, leftStart, nowRow + 1, rowNums)
            printRow(tree.left, row, leftStart, nowRow + 1, rowNums)


NR = input().split(" ")
n = int(NR[0])
rootData = int(NR[1])
nodes = [0]
length = 0
for i in range(n):
    node = list(map(int, input().split(" ")))
    if length < node[0]:
        for i in range(node[0] - length):
            nodes.append(0)
        length = node[0]
    nodes[node[0]] = node
root = nodes[rootData]
tree = createTree(nodes, root)
leftStart = True
length = findLength(tree)
for i in range(1, length + 1):
    print("Level " + str(i) + " :", end="")
    a = []
    printRow(tree, i, leftStart, 1, a)
    for j in a:
        print(" " + str(j), end="")
    print("")
for i in range(1, length + 1):
    if leftStart:
        string = "left to right"
    else:
        string = "right to left"
    print("Level " + str(i) + " from " + string + ":", end="")
    a = []
    printRow(tree, i, leftStart, 1, a)
    for j in a:
        print(" " + str(j), end="")
    print("")
    leftStart = not (leftStart)

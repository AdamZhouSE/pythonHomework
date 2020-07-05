class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def test():
    nroot = input().split()
    n = int(nroot[0])
    root_id = int(nroot[1])
    nodes = []
    for _ in range(0, n):
        node = input()
        node = node.split()
        node = list(map(int, node))
        nodes.append(node)
    root = createBT(nodes, root_id)
    levels = []
    getLevels(root, levels)
    printByLevels(levels)
    printByZigZag(levels)


def createBT(nodes, root_id):
    if root_id == 0:
        return None
    for node in nodes:
        if node[0] == root_id:
            left = createBT(nodes, node[1])
            right = createBT(nodes, node[2])
            return Node(root_id, left, right)


def getLevels(root, levels):
    level = [root]
    levels.append(level)
    bfs(level, levels)


def bfs(level, levels):
    newLevel = []
    for node in level:
        if node.left is not None:
            newLevel.append(node.left)
        if node.right is not None:
            newLevel.append(node.right)
    if not newLevel:
        return
    else:
        levels.append(newLevel)
        bfs(newLevel, levels)


def printByLevels(levels):
    for i in range(0, len(levels)):
        print('Level ' + str(i + 1) + ' :', end='')
        string = ''
        for node in levels[i]:
            string = string + ' ' + str(node.data)
        print(string)

def printByZigZag(levels):
    for i in range(0,len(levels)):
        if i%2==0:
            print('Level ' + str(i + 1) +' from left to right:',end='')
            string = ''
            for node in levels[i]:
                string = string + ' ' + str(node.data)
            print(string)
        else:
            print('Level ' + str(i + 1) + ' from right to left:', end='')
            string = ''
            re_level=reversed(levels[i])
            for node in re_level:
                string = string + ' ' + str(node.data)
            print(string)

test()
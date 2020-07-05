# 5
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
    nodeToQuery = int(input())
    sequence = inOrder(root)
    if sequence.index(nodeToQuery) == len(sequence) - 1:
        print(0)
    else:
        print(sequence[sequence.index(nodeToQuery) + 1])


def createBT(nodes, root_id):
    if root_id == 0:
        return None
    for node in nodes:
        if node[0] == root_id:
            left = createBT(nodes, node[1])
            right = createBT(nodes, node[2])
            return Node(root_id, left, right)


def inOrder(root):
    if root is None:
        return []
    left = inOrder(root.left)
    element = root.data
    right = inOrder(root.right)
    lis = left + [element] + right
    return lis


test()
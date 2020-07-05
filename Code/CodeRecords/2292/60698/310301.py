import copy


class Node:
    def __init__(self, value, lch=None, rch=None, parent=None, side=-1):
        self.value = value
        self.lch = lch
        self.rch = rch
        self.parent = parent
        self.side = side


def test():
    nroot = input().split()
    n = int(nroot[0])
    root = int(nroot[1])
    nodes = [Node(i) for i in range(0, n + 1)]
    root = nodes[root]
    for _ in range(0, n):
        line = input()
        line = line.split()
        fa = int(line[0])
        left = int(line[1])
        right = int(line[2])
        if left != 0:
            nodes[fa].lch = nodes[left]
            nodes[left].side = 0
            nodes[left].parent = nodes[fa]

        if right != 0:
            nodes[fa].rch = nodes[right]
            nodes[right].side = 1
            nodes[right].parent = nodes[fa]
    res = get_max_topo(root, nodes)
    print(res)


def get_max_topo(root, nodes):
    for i in range(0, len(nodes)):
        node = nodes[i]
        if node.side == 0 and node.value > node.parent.value:
            node.parent.lch = None
            node.parent = None
            node.side = -1
        elif node.side == 1 and node.value < node.parent.value:
            node.parent.rch = None
            node.parent = None
            node.side = -1
    res = 0
    for i in range(0, len(nodes)):
        node = nodes[i]
        if node.side == -1:
            count = nodes_count(node)
            if res < count:
                res = count
    return res


def nodes_count(root):
    nodes_in_BST = [root]
    dfs(root, nodes_in_BST)
    return len(nodes_in_BST)


def dfs(root, nodes_in_BST):
    if root.lch is not None:
        nodes_in_BST.append(root.lch)
        dfs(root.lch, nodes_in_BST)
    if root.rch is not None:
        nodes_in_BST.append(root.rch)
        dfs(root.rch, nodes_in_BST)


test()

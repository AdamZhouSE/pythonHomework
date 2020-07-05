class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def test():
    nr = input().split()
    n = int(nr[0])
    r = int(nr[1])
    nodes = [Node(i) for i in range(0, n + 1)]
    root = nodes[r]
    for _ in range(0, n):
        line = input().split()
        fa = int(line[0])
        lch = int(line[1])
        rch = int(line[2])
        if lch != 0:
            nodes[fa].left = nodes[lch]
            nodes[lch].parent = nodes[fa]
        if rch != 0:
            nodes[fa].right = nodes[rch]
            nodes[rch].parent = nodes[fa]
    m = int(input())
    for _ in range(0, m):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        ancestor = getAncestor(root, u, v, nodes)
        print(ancestor.value)
        


def getAncestor(root, u, v, nodes):
    p = nodes[u]
    while True:
        if isDescendant(p, v, nodes):
            return p
        else:
            p = p.parent
            

def isDescendant(parent, v_index, nodes):
    descendant = []
    getDescendant(parent, descendant)
    if nodes[v_index] in descendant:
        return True
    else:
        return False


def getDescendant(parent, descendant):
    descendant.append(parent)
    if parent.left is not None:
        getDescendant(parent.left, descendant)
    if parent.right is not None:
        getDescendant(parent.right, descendant)

test()
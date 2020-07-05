class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def test():
    n = int(input())
    nodes = [Node(i) for i in range(0, n + 1)]
    for _ in range(0, n-1):
        edge = input().split()
        edge = list(map(int, edge))
        p = edge[0]
        c = edge[1]
        if nodes[p].left is None:
            nodes[p].left = nodes[c]
        else:
            nodes[p].right = nodes[c]
        nodes[c].parent = nodes[p]
    uv = input().split()
    u = int(uv[0])
    v = int(uv[1])
    root = nodes[1]
    depth = getDepth(root)
    width = getWidth(root)
    uvdis = getDist(root, u, v, nodes)
    print(depth)
    print(width)
    print(uvdis,end='')


def getDepth(root):
    if root is None:
        return 0
    else:
        return max(getDepth(root.left), getDepth(root.right)) + 1


def getWidth(root):
    level = [root]
    width = 1
    now_width = 1
    while level:
        while now_width != 0:
            if level[0].left is not None:
                level.append(level[0].left)
            if level[0].right is not None:
                level.append(level[0].right)
            level.pop(0)
            now_width = now_width - 1
        if width < len(level):
            width = len(level)
        now_width = len(level)
    return width


def getDist(root, u, v, nodes):
    u2a = [0]
    ancestor = getAncestor(root, u, v, nodes, u2a)
    u2a = u2a[0]
    a2v = [0]
    geta2v(ancestor, v, nodes, a2v)
    res = u2a * 2 + a2v[0]
    return res


def geta2v(ancestor, v, nodes, a2v):
    if nodes[v] != ancestor:
        a2v[0] = a2v[0] + 1
        geta2v(ancestor, nodes[v].parent.value, nodes, a2v)


def getAncestor(root, u, v, nodes, u2a):
    p = nodes[u]
    while True:
        if isDescendant(p, v, nodes):
            return p
        else:
            p = p.parent
            u2a[0] = u2a[0] + 1


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

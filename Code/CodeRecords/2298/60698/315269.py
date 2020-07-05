class Node:
    def __init__(self, value, lch=None, rch=None, par=None):
        self.value = value
        self.lch = lch
        self.rch = rch
        self.par = par


def test():
    n = int(input())
    nums = list(map(int, input().split()))
    nodes = []
    root = None
    for i in range(0, n):
        nodes.append(Node(nums[i]))
    for i in range(0, n):
        node = nodes[i]
        if root is None:
            root = node
            print(-1)
        else:
            insert(node, root)
            print(node.par.value)


def insert(node, root):
    val = node.value
    r_val = root.value
    if val < r_val:
        if root.lch is None:
            root.lch = node
            node.par = root
        else:
            insert(node, root.lch)
    elif val > r_val:
        if root.rch is None:
            root.rch = node
            node.par = root
        else:
            insert(node, root.rch)

test()
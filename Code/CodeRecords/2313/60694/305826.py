# class TreeNode:
#     def __init__(self, x = -1, left = None, right = None):
#         self.data = x
#         self.lhs = left
#         self.rhs = right
#
#
# class Tree:
#     def __init__(self, root: TreeNode):
#         self.root = root


from collections import defaultdict
tree = defaultdict(list)


def isBST(t):
    l = []

    def inOrder(t):
        if t == 0:
            return
        inOrder(tree[t][0])
        l.append(t)
        inOrder(tree[t][1])
    inOrder(t)
    if sorted(l) == l:
        return "true"
    return "false"


def isCBT(t):
    queue = [t]
    flag_isLeaf = False
    while len(queue):
        node = queue[0]
        lhs, rhs = tree[node][0], tree[node][1]
        queue.pop(0)
        if (not lhs and rhs) or (flag_isLeaf and (lhs or rhs)):
            return "false"
        if lhs:
            queue.append(tree[node][0])
        if rhs:
            queue.append(tree[node][1])
        if not (lhs and rhs):
            flag_isLeaf = True
    return "true"


n, root = map(int, input().split())
for _ in range(n):
    fa, lch, rch = map(int, input().split())
    tree[fa] = [lch, rch]
print(isBST(root))
print(isCBT(root))

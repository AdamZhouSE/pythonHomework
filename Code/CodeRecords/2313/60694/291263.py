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
tree[0] = ["I'm leaf"]


def isBST(t):
    l = []

    def inOrder(t):
        if tree[t] == ["I'm leaf"]:
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
    flag = False
    while len(queue):
        node = queue[0]
        queue.pop(0)
        if flag:
            if (tree[node][0] or tree[node][1]) or (not tree[node][0] and tree[node][1]):
                return "false"
        if tree[node][0]:
            queue.append(tree[node][0])
        if tree[node][1]:
            queue.append(tree[node][1])
        else:
            flag = True
    return "true"


n, root = map(int, input().split())
for _ in range(n):
    fa, lch, rch = map(int, input().split())
    tree[fa] = [lch, rch]
print(isBST(root))
print(isCBT(root))

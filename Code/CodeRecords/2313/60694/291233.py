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
l = []
def inOrder(t):
    if tree[t] == ["X"]:
        return
    inOrder(tree[t][0])
    l.append(t)
    inOrder(tree[t][1])
def isBST(t):
    if sorted(l) == l:
        return "true"
    return "false"


def isCBT(t):
    queue = []
    queue.append(t)
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
tree[0] = ["X"]
for _ in range(n):
    fa, lch, rch = map(int, input().split())
    tree[fa].append(lch)
    tree[fa].append(rch)
inOrder(root)
print(isBST(root))
print(isCBT(root))

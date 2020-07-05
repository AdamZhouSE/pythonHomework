from collections import defaultdict


class SuperNode:
    def __init__(self):
        self.size = 0
        self.is_BST = True
        self.max_n = float('-inf')
        self.min_n = float('inf')


def dfs(r):
    if r == 0:
        return SuperNode()
    now = SuperNode()
    left = dfs(tree[r][0])
    right = dfs(tree[r][1])
    now.max_n = max(right.max_n, r)
    now.min_n = min(left.min_n, r)
    if left.is_BST and right.is_BST and left.max_n < r < right.min_n:
        now.size = 1 + left.size + right.size
    else:
        now.size = max(left.size, right.size)
        now.is_BST = False
    return now


ns, root = map(int, input().split(' '))
tree = defaultdict(list)
for n in range(ns):
    fa, lch, rch = map(int, input().split(' '))
    tree[fa] = [lch, rch]
print(dfs(root).size)

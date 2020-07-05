class Tree:
    val = 0
    left = None
    right = None

    def __init__(self, x):
        self.val = x


mid = list(map(int, input().split(" ")))
succ = list(map(int, input().split(" ")))
store = dict()


def generate(Mid, Succ):
    if len(Succ) == 0:
        return None
    root = Tree(Succ[-1])
    if len(Succ) == 1:
        return root
    i = 0
    while Mid[i] != Succ[-1]:
        i += 1
    root.left = generate(Mid[0:i], Succ[0:i])
    root.right = generate(Mid[i + 1:], Succ[i:-1])
    return root


Root = generate(mid, succ)
store = dict()


def dfs(root, x):
    if root is None:
        return
    if root.right is None and root.left is None:
        store[x + root.val] = root.val
    else:
        dfs(root.left, x + root.val)
        dfs(root.right, x + root.val)


dfs(Root, 0)
print(store[sorted(store)[0]])

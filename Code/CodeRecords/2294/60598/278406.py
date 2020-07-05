class Tree:
    val = ""
    left = None
    right = None

    def __init__(self, x):
        self.val = x


def generate(pre, mid):
    if len(pre) == 0:
        return None
    first = pre[0]
    root = Tree(first)
    i = 0
    while mid[i] != first:
        i += 1
    root.left = generate(pre[1:1 + i], mid[0:i])
    root.right = generate(pre[i + 1:], mid[i + 1:])
    return root


def succ(root):
    if root is None:
        return ""
    l = succ(root.left)
    r = succ(root.right)
    return l + r + root.val


while 1:
    try:

        pre = input()
        mid = input()
        print(succ(generate(pre, mid)))
    except EOFError:
        break

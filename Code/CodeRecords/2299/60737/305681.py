class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getv(self):
        return self.value


class Tree:
    def __init__(self):
        self.nodes = {}


def crTree(s):
    tree = Tree()
    c = int(s[0])
    tree.nodes[c] = TreeNode(c)
    root = tree.nodes[c]
    for i in range(1, len(s)):
        root = insert(tree, root, int(s[i]))
    return root


def insert(tree, head, data):
    if not head:
        tree.nodes[data] = TreeNode(data)
        ndata = tree.nodes[data]
        return ndata
    if data < head.getv():
        head.left = insert(tree, head.left, data)
    else:
        head.right = insert(tree, head.right, data)
    return head


def prev(head):
    res = ""
    if not head:
        return res
    res += str(head.getv())
    res += prev(head.left)
    res += prev(head.right)
    return res


if __name__ == "__main__":
    n = int(input())
    s0 = input()
    ta = crTree(s0)
    sam = prev(ta)
    while n:
        sn = input()
        tn = crTree(sn)
        an = prev(tn)
        print("YES" if sam==an else "NO")
        n -= 1

    
    
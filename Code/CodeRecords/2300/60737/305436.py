index = 0


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
    global index
    tree = Tree()
    if index<len(s):
        c = s[index]
        if c != '#':
            if c not in tree.nodes:
                tree.nodes[c] = TreeNode(c)
            root = tree.nodes[c]
            index += 1
            root.left = crTree(s)
            root.right = crTree(s)
            return root
        else:
            index += 1
            return
    else:
        return


def btorder(r):
    if not r:
        return
    btorder(r.left)
    print(r.getv(), end=" ")
    btorder(r.right)


if __name__ == "__main__":
    s = input()
    head = crTree(s)
    btorder(head)

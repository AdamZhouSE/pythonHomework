class Tree:
    allNode = {}

    def __init__(self, n, l, r):
        self.allNode[n] = self
        self.name = n
        self.left = l
        self.right = r

    def p(self):
        print(self.allNode)

    @staticmethod
    def getInfx(root, res):
        if root.name == YEZI:
            return
        Tree.getInfx(root.left, res)
        res.append(str(root.name))
        Tree.getInfx(root.right, res)

    @staticmethod
    def sum(node):
        if node.name == YEZI:
            return 0
        temp = Tree.sum(node.left) + Tree.sum(node.right)
        su = temp + node.name
        node.name = temp
        return su


def createTree(prefix, infix):
    if len(prefix) == 0:
        return YEZI
    root = prefix[0]
    index = infix.index(root)
    l = createTree(prefix[1:1 + index], infix[:index])
    r = createTree(prefix[1 + index:], infix[index + 1:])
    Tree(root, Tree.allNode[l], Tree.allNode[r])
    return root


YEZI = -99999
if __name__ == '__main__':
    Tree.allNode[YEZI] = Tree(YEZI, 0, 0)
    prefix = list(map(int, input().split()))
    infix = list(map(int, input().split()))
    root = Tree.allNode[createTree(prefix, infix)]
    Tree.sum(root)
    res = []
    Tree.getInfx(root, res)
    print(" ".join(res))

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
    def ZigZag(root):
        res = []
        stack = [root]
        while len(stack) != 0:
            nstack = []
            tres = []
            while len(stack) != 0:
                # tres = []
                temp = stack.pop(0)
                tres.append(str(temp))
                if Tree.allNode[temp].left != 0:
                    nstack.append(Tree.allNode[temp].left)
                if Tree.allNode[temp].right != 0:
                    nstack.append(Tree.allNode[temp].right)
            stack = nstack
            res.append(" ".join(tres))
        return res


def printres(res):
    for i in range(len(res)):
        print("Level", i + 1, ": " + res[i])
    for i in range(len(res)):
        if i % 2 == 0:
            print("Level", i + 1, "from left to right: " + res[i])
        else:
            print("Level", i + 1, "from right to left: " + res[i][::-1])


if __name__ == '__main__':
    num, root = list(map(int, input().split()))
    for i in range(num):
        n, l, r = list(map(int, input().split()))
        Tree(n, l, r)
    res = Tree.ZigZag(root)
    # print(res)
    printres(res)


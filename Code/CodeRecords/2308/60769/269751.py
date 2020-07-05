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
    def zhongxu(root, res):
        if root == 0:
            return
        Tree.zhongxu(Tree.allNode[root].left, res)
        res.append(root)
        Tree.zhongxu(Tree.allNode[root].right, res)


if __name__ == '__main__':
    num, root = list(map(int, input().split()))
    for i in range(num):
        n, l, r = list(map(int, input().split()))
        Tree(n, l, r)
    res = []
    Tree.zhongxu(root, res)
    n = int(input())
    if res[-1] == n:
        print(0)
    else:
        print(res[res.index(n) + 1])

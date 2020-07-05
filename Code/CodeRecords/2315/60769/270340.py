class Tree:
    allNode = {}

    def __init__(self, n, l, r):
        self.allNode[n] = self
        self.name = n
        self.left = l
        self.right = r

    @staticmethod
    def getHeight(root):
        if root == YEZI:
            return 0
        else:
            return 1 + max([Tree.getHeight(Tree.allNode[root].left), Tree.getHeight(Tree.allNode[root].right)])


YEZI = -99999
if __name__ == '__main__':
    Tree.allNode[YEZI] = YEZI
    n = int(input())
    dict = {}
    for i in range(n):
        dict[i] = []
    for i in range(n-1):
        fa, son = list(map(int, input().split()))
        dict[fa].append(son)
    for i in dict.keys():
        if len(dict[i]) == 2:
            Tree(i, dict[i][0], dict[i][1])
        elif len(dict[i]) == 1:
            Tree(i, dict[i][0], YEZI)
        elif len(dict[i]) == 0:
            Tree(i, YEZI, YEZI)
    print(Tree.getHeight(0))
class Tree:
    allNode = {}

    def __init__(self, n, l, r):
        self.allNode[n] = self
        self.name = n
        self.left = l
        self.right = r

    @staticmethod
    def search(root, target):
        if root == target:
            return True
        elif root == YEZI:
            return False
        else:
            lres = False
            if Tree.allNode[root].left != YEZI:
                lres = Tree.search(Tree.allNode[root].left, target)
            if lres:
                return lres
            rres = False
            if Tree.allNode[root].right != YEZI:
                rres = Tree.search(Tree.allNode[root].right, target)
            if rres:
                return True
            else:
                False


def printres(res):
    for i in range(len(res)):
        print("Level", i + 1, ": " + res[i])
    for i in range(len(res)):
        if i % 2 == 0:
            print("Level", i + 1, "from left to right : " + res[i])
        else:
            print("Level", i + 1, "from right to left : " + res[i][::-1])


YEZI = 0
if __name__ == '__main__':
    Tree.allNode[YEZI] = YEZI
    num, root = list(map(int, input().split()))
    record = []
    for i in range(num):
        n, l, r = list(map(int, input().split()))
        Tree(n, l, r)
        record.append([n,l,r])

    a, b = list(map(int, input().split()))
    try:
        while True:
            la = False
            lb = False
            rb = False
            ra = False

            if Tree.allNode[root].left != YEZI:
                la = Tree.search(Tree.allNode[root].left, a)
                lb = Tree.search(Tree.allNode[root].left, b)

            if Tree.allNode[root].right != YEZI:
                ra = Tree.search(Tree.allNode[root].right, a)
                rb = Tree.search(Tree.allNode[root].right, b)

            if (la and rb) or (lb and ra):
                break
            elif la and lb:
                root = Tree.allNode[root].left
            else:
                root = Tree.allNode[root].right
        print(root)
    except:
        print(record)
        print(root)
        print(a,b)
    



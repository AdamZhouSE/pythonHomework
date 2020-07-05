read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]


class Tree:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

    def insert(self, v):
        if v > self.v:
            if self.right:
                self.right.insert(v)
            else:
                self.right = Tree(v)
        else:
            if self.left:
                self.left.insert(v)
            else:
                self.left = Tree(v)


def same(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if not t1.v == t2.v:
        return False
    if not same(t1.left, t2.left):
        return False
    if not same(t1.right, t2.right):
        return False
    return True


def get_tree(xs):
    root = Tree(xs[0])
    for i in range(1, len(xs)):
        root.insert(xs[i])
    return root


if __name__ == '__main__':
    n = read()
    init = get_tree(input())
    for _ in range(n):
        one = get_tree(input())
        if same(one, init):
            print('YES')
        else:
            print('NO')

read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]


class SimpleTree:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.v = v

    @staticmethod
    def build(data, root=None):
        try:
            if root is None:
                root = [0]

            v = data[root[0]]
            root[0] += 1
            if v == '#':
                return None
            res = SimpleTree(v)
            res.left = SimpleTree.build(data, root)
            res.right = SimpleTree.build(data, root)
            return res
        except:
            return None

    def mid_iter(self):
        self.left.mid_iter() if self.left else 0
        print(self.v, end=' ')
        self.right.mid_iter() if self.right else 0


if __name__ == '__main__':
    tree = SimpleTree.build(input())
    tree.mid_iter()

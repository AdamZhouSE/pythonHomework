class Node:
    def __init__(self, value):
        self.val = value
        self.lch = None
        self.rch = None
        self.height = 1
        self.weight = 0

    def insert_children(self, left, right, power):
        self.lch = Node(left)
        self.rch = Node(right)
        self.lch.height = self.height + 1
        self.rch.height = self.height + 1
        self.lch.weight = power
        self.rch.weight = power

    def insert_node(self, value, left, right, power):
        if self is not None:
            if self.val != value:
                if self.lch is not None:
                    self.lch.insert_node(value, left, right, power)
                if self.rch is not None:
                    self.rch.insert_node(value, left, right, power)
            else:
                self.insert_children(left, right, power)

    def max_path_from_this_node(self, summary):
        # 队列
        q = [self.lch, self.rch]
        weights = [self.lch.weight, self.rch.weight]
        res = 0
        path = 1
        while len(q) > 0:
            if summary in weights:
                res = path
            length = len(q)
            for i in range(length):
                # 将同层节点依次出队
                node = q.pop(0)
                wgt = weights.pop(0)
                if node.lch is not None:
                    # 非空左孩子入队
                    q.append(node.lch)
                    weights.append(node.lch.weight + wgt)
                if node.rch is not None:
                    # 非空右孩子入队
                    q.append(node.rch)
                    weights.append(node.rch.weight + wgt)
            path += 1
        return res

    def find_max_path(self, summary):
        # 队列
        q = [self]
        res = self.max_path_from_this_node(summary)
        while len(q) != 0:
            paths = []
            length = len(q)
            for i in range(length):
                # 将同层节点依次出队
                node = q.pop(0)
                if node.lch.val != 0:
                    # 非空左孩子入队
                    q.append(node.lch)
                    paths.append(node.lch.max_path_from_this_node(summary))
                if node.rch.val != 0:
                    # 非空右孩子入队
                    q.append(node.rch)
                    paths.append(node.rch.max_path_from_this_node(summary))
            if len(paths) > 0:
                res = max(res, max(paths))
        return res


if __name__ == '__main__':
    basic = input().split()
    root = Node(int(basic[1]))
    for i in range(int(basic[0])):
        inf = input().split()
        root.insert_node(int(inf[0]), int(inf[1]), int(inf[2]), int(inf[3]))
    print(root.find_max_path(int(input())))
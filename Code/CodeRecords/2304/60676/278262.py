class Node:
    def __init__(self, value):
        self.val = value
        self.lch = None
        self.rch = None

    def insert_children(self, left, right):
        self.lch = Node(left)
        self.rch = Node(right)

    def insert_node(self, value, left, right):
        if self is not None:
            if self.val != value:
                if self.lch is not None:
                    self.lch.insert_node(value, left, right)
                if self.rch is not None:
                    self.rch.insert_node(value, left, right)
            else:
                self.insert_children(left, right)

    def level_order(self):
        if self is None:
            return []
        # 队列
        q = [self]
        res = []
        while len(q) != 0:
            res.append([])
            for i in range(len(q)):
                if q[i] != 0:
                    res[-1].append(q[i].val)
            length = len(q)
            for i in range(length):
                # 将同层节点依次出队
                node = q.pop(0)
                if node.lch is not None and node.lch.val != 0:
                    # 非空左孩子入队
                    q.append(node.lch)
                if node.rch is not None and node.rch.val != 0:
                    # 非空右孩子入队
                    q.append(node.rch)
        return res

    def zigzag_order(self):
        res = self.level_order()
        for i in range(1, len(res), 2):
            res[i].reverse()
        return res


if __name__ == '__main__':
    basic = input().split()
    root = Node(int(basic[1]))
    for i in range(int(basic[0])):
        inf = input().split()
        root.insert_node(int(inf[0]), int(inf[1]), int(inf[2]))
    lo = root.level_order()
    zo = root.zigzag_order()
    for i in range(len(lo)):
        print('Level {} :'.format(i+1), end='')
        for j in range(len(lo[i])):
            print(' {}'.format(lo[i][j]), end='')
        print()
    direction = ['left', 'right']
    for i in range(len(zo)):
        print('Level {} from {} to {}:'.format(i + 1, direction[i % 2], direction[1 - i % 2]), end='')
        for j in range(len(zo[i])):
            print(' {}'.format(zo[i][j]), end='')
        print()
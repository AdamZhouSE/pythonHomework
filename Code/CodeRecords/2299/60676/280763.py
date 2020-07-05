class Node:
    def __init__(self, value):
        self.val = value
        self.lch = None
        self.rch = None

    def insert_child(self, child):
        curr = self
        while True:
            if child < curr.val:
                if curr.lch is None:
                    curr.lch = Node(child)
                    break
                else:
                    curr = curr.lch
            else:
                if curr.rch is None:
                    curr.rch = Node(child)
                    break
                else:
                    curr = curr.rch

    def insert_nodes(self, nodes: str):
        for char in nodes:
            self.insert_child(int(char))

    def prefix_traversal(self):
        res = [self.val]
        if self.lch is not None:
            res += self.lch.prefix_traversal()
        if self.rch is not None:
            res += self.rch.prefix_traversal()
        return res


def compare(p1: list, p2: list):
    if len(p1) == len(p2):
        for i in range(len(p1)):
            if p1[i] != p2[i]:
                return 'NO'
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    result = []
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            tmp = input()
            std_tree = Node(int(tmp[0]))
            std_tree.insert_nodes(tmp[1:])
            std_pt = std_tree.prefix_traversal()
            for i in range(n):
                tmp = input()
                cmp_tree = Node(int(tmp[0]))
                cmp_tree.insert_nodes(tmp[1:])
                cmp_pt = cmp_tree.prefix_traversal()
                result.append(compare(std_pt, cmp_pt))
    for r in result:
        print(r)
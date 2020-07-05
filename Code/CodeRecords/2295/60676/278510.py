class Node:
    def __init__(self, value):
        self.val = value
        self.lch = None
        self.rch = None
        self.parent = None
        self.height = 1

    def insert_children(self, left, right):
        self.lch = Node(left)
        self.rch = Node(right)
        self.lch.parent = self
        self.rch.parent = self
        self.lch.height = self.height + 1
        self.rch.height = self.height + 1

    def insert_node(self, value, left, right):
        if self is not None:
            if self.val != value:
                if self.lch is not None:
                    self.lch.insert_node(value, left, right)
                if self.rch is not None:
                    self.rch.insert_node(value, left, right)
            else:
                self.insert_children(left, right)

    def find_node(self, value):
        if self.val == value:
            return self
        else:
            if self.lch is not None:
                res = self.lch.find_node(value)
                if res is not None:
                    return res
            if self.rch is not None:
                res = self.rch.find_node(value)
                if res is not None:
                    return res

    def find_first_common_parent(self, value1, value2):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)
        if node1.height < node2.height:
            for i in range(node2.height - node1.height):
                node2 = node2.parent
        else:
            for i in range(node1.height - node2.height):
                node1 = node1.parent
        while node1 != node2:
            node1 = node1.parent
            node2 = node2.parent
        return node1.val


if __name__ == '__main__':
    basic = input().split()
    root = Node(int(basic[1]))
    for i in range(int(basic[0])):
        inf = input().split()
        root.insert_node(int(inf[0]), int(inf[1]), int(inf[2]))
    a = input().split()
    print(root.find_first_common_parent(int(a[0]), int(a[1])))
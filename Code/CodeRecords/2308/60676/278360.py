class Node:
    def __init__(self, value):
        self.val = value
        self.lch = None
        self.rch = None
        self.parent = None

    def insert_children(self, left, right):
        self.lch = Node(left)
        self.rch = Node(right)
        self.lch.parent = self
        self.rch.parent = self

    def insert_node(self, value, left, right):
        if self is not None:
            if self.val != value:
                if self.lch is not None:
                    self.lch.insert_node(value, left, right)
                if self.rch is not None:
                    self.rch.insert_node(value, left, right)
            else:
                self.insert_children(left, right)

    def find_infix_next(self, value):
        if self is not None:
            if self.val == value:
                if self.rch.val != 0:
                    tmp = self.rch
                    while tmp.lch.val != 0:
                        tmp = tmp.lch
                    return tmp.val
                else:
                    if self == self.parent.lch:
                        return self.parent.val
                    else:
                        tmp = self
                        while tmp.parent is not None and tmp == tmp.parent.rch:
                            tmp = tmp.parent
                        if tmp.parent is None:
                            return 0
                        return tmp.parent.val
            else:
                if self.rch.val != 0:
                    t = self.rch.find_infix_next(value)
                    if t is not None:
                        return t
                if self.lch.val != 0:
                    t = self.lch.find_infix_next(value)
                    if t is not None:
                        return t


if __name__ == '__main__':
    basic = input().split()
    root = Node(int(basic[1]))
    for i in range(int(basic[0])):
        inf = input().split()
        root.insert_node(int(inf[0]), int(inf[1]), int(inf[2]))
    print(root.find_infix_next(int(input())))
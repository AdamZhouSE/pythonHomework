class Node:

    def __init__(self, value):
        self.val = value
        self.lch = None
        self.rch = None
        self.height = 1

    def insert_children(self, child):
        if self.lch is None:
            self.lch = Node(child)
            self.lch.height = self.height + 1
        else:
            self.rch = Node(child)
            self.rch.height = self.height + 1

    def insert_node(self, value, child):
        if self is not None:
            if self.val != value:
                if self.lch is not None:
                    self.lch.insert_node(value, child)
                if self.rch is not None:
                    self.rch.insert_node(value, child)
            else:
                self.insert_children(child)

    def get_height_of_tree(self):
        tmp = self.height
        if self.lch is not None:
            tmp = max(self.lch.get_height_of_tree(), tmp)
        if self.rch is not None:
            tmp = max(self.rch.get_height_of_tree(), tmp)
        return tmp


if __name__ == '__main__':
    root = Node(int(0))
    for i in range(int(input())-1):
        inf = input().split()
        root.insert_node(int(inf[0]), int(inf[1]))
    print(root.get_height_of_tree())
class BinaryTree:
    def __init__(self, value):
        self.father = None
        self.left_node = None
        self.right_node = None
        self.value = value
        self.be_changed = False
        self.top = 0

    def set_father(self, x):
        self.father = x

    def set_left(self, x):
        self.left_node = x
        self.left_node.set_father(self)

    def set_right(self, x):
        self.right_node = x
        self.right_node.set_father(self)

    def max_top(self):
        if self.be_changed:
            return self.top
        else:
            result = 1
            if self.left_node is not None:
                if self.left_node.value < self.value:
                    result += self.left_node.max_top()
            if self.right_node is not None:
                if self.right_node.value > self.value:
                    result += self.right_node.max_top()
            self.be_changed = True
            self.top = result
            return result


if __name__ == '__main__':
    n, root = map(int, input().strip().split(" "))
    nodes = [BinaryTree(i) for i in range(0, n + 1)]
    for i in range(0, n):
        x, y, z = map(int, input().strip().split(" "))
        if y != 0:
            nodes[x].set_left(nodes[y])
            nodes[y].set_father(nodes[x])
        if z != 0:
            nodes[x].set_right(nodes[z])
            nodes[z].set_father(nodes[x])
    tree = nodes[root]
    result = 0
    for i in range(1, n + 1):
        result = max(result, nodes[i].max_top())
    print(result)

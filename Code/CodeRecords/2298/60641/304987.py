class BinaryTree:
    def __init__(self, value):
        self.father = None
        self.left_node = None
        self.right_node = None
        self.value = value

    def set_father(self, x):
        self.father = x

    def set_left(self, x):
        self.left_node = BinaryTree(x)
        self.left_node.set_father(self)

    def set_right(self, x):
        self.right_node = BinaryTree(x)
        self.right_node.set_father(self)

    def insert(self, node):
        result = 0
        if node.value < self.value:
            if self.left_node is not None:
                result = self.left_node.insert(node)
            else:
                self.left_node = node
                result = self.value
        elif node.value > self.value:
            if self.right_node is not None:
                result = self.right_node.insert(node)
            else:
                self.right_node = node
                result = self.value
        return result


if __name__ == '__main__':
    n = int(input().strip())
    values = list(map(int, input().strip().split(" ")))
    tree = None
    for i in range(0, n):
        if tree is None:
            tree = BinaryTree(values[i])
            print(-1)
        else:
            print(tree.insert(BinaryTree(values[i])))

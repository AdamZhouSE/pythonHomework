class BinaryTree:
    def __init__(self):
        self.father = None
        self.left_node = None
        self.right_node = None
        self.value = None

    def set_father(self, x):
        self.father = x

    def set_left(self, x):
        self.left_node = x
        self.left_node.set_father(self)

    def set_right(self, x):
        self.right_node = x
        self.right_node.set_father(self)

    def set_value(self, x):
        self.value = x

    def find_path(self):
        left_result = []
        right_result = []
        if self.left_node is not None:
            left_result = self.left_node.find_path()
        if self.right_node is not None:
            right_result = self.right_node.find_path()
        result = left_result + right_result
        length = len(result)
        if length == 0:
            result = [[self.value]]
        else:
            result += [[self.value]]
            for i in range(0, length):
                if self.left_node is not None:
                    if result[i][0] == self.left_node.value:
                        result.append([self.value] + result[i])
                if self.right_node is not None:
                    if result[i][0] == self.right_node.value:
                        result.append([self.value] + result[i])
        return result


if __name__ == '__main__':
    n, root = map(int, input().strip().split(" "))
    nodes = [BinaryTree() for i in range(0, n + 1)]
    tree = None
    for i in range(1, n + 1):
        x, y, z, v = map(int, input().strip().split(" "))
        if y != 0:
            nodes[x].set_left(nodes[y])
            nodes[y].set_father(nodes[x])
        if z != 0:
            nodes[x].set_right(nodes[z])
            nodes[z].set_father(nodes[x])
        nodes[x].set_value(v)
    tree = nodes[root]
    key = int(input().strip())
    result = sorted(tree.find_path(), key=lambda x: len(x), reverse=True)
    for i in range(0, len(result)):
        if sum(result[i]) == key:
            print(len(result[i]))
            break

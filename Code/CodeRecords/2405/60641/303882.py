class BinaryTree:
    def __init__(self, value):
        self.father = None
        self.left_node = None
        self.right_node = None
        self.value = value

    def set_father(self, x):
        self.father = x

    def set_son(self, x):
        if self.left_node is None:
            self.left_node = x
        else:
            self.right_node = x

    def get_depth(self, node):
        result = -1
        if self.value == node.value:
            result = 0
        else:
            if self.left_node is not None:
                temp = self.left_node.get_depth(node)
                if temp != -1:
                    result = 1 + temp
            if self.right_node is not None:
                temp = self.right_node.get_depth(node)
                if temp != -1:
                    result = 1 + temp
        return result

    def max_depth(self):
        result = 1
        left_depth = 0
        right_depth = 0
        if self.left_node is not None:
            left_depth = self.left_node.max_depth()
        if self.right_node is not None:
            right_depth = self.right_node.max_depth()
        result += max(left_depth, right_depth)
        return result

    def max_width(self):
        result = 1
        one_line_nodes = [self]
        while len(one_line_nodes) != 0:
            length = len(one_line_nodes)
            result = max(result, length)
            for i in range(0, length):
                if one_line_nodes[i].left_node is not None:
                    one_line_nodes.append(one_line_nodes[i].left_node)
                if one_line_nodes[i].right_node is not None:
                    one_line_nodes.append(one_line_nodes[i].right_node)
            one_line_nodes = one_line_nodes[length:]
        return result


if __name__ == '__main__':
    n = int(input().strip())
    nodes = [BinaryTree(i) for i in range(0, n + 1)]
    for i in range(0, n - 1):
        x, y = map(int, input().strip().split(" "))
        nodes[y].set_father(nodes[x])
        nodes[x].set_son(nodes[y])
    tree = nodes[1]

    node_1, node_2 = map(int, input().strip().split(" "))
    common_node = 0
    parent_1 = node_1
    parent_2 = node_2
    while tree.get_depth(nodes[parent_1]) != tree.get_depth(nodes[parent_2]) or common_node == 0:
        if tree.get_depth(nodes[parent_1]) > tree.get_depth(nodes[parent_2]):
            parent_1 = nodes[parent_1].father.value
            continue
        elif tree.get_depth(nodes[parent_1]) < tree.get_depth(nodes[parent_2]):
            parent_2 = nodes[parent_2].father.value
            continue
        if parent_1 == parent_2:
            common_node = parent_1
            break
        else:
            parent_1 = nodes[parent_1].father.value
            parent_2 = nodes[parent_2].father.value
    distance = (tree.get_depth(nodes[node_1]) - tree.get_depth(nodes[common_node])) * 2 + tree.get_depth(
        nodes[node_2]) - tree.get_depth(nodes[
                                            common_node])
    print("\n".join([str(tree.max_depth()), str(tree.max_width()), str(distance)]), end="")

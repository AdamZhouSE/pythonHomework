class Node:
    def __init__(self, number, value):
        self.value = value
        self.number = number


class Binary_tree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def cal_value(self):
        if self.root is None:
            return 1
        else:
            if self.left is None:
                if self.right is None:
                    return self.root.value
                else:
                    return self.right.cal_value() + self.root.value
            else:
                if self.right is None:
                    return self.root.value + self.left.cal_value()
                else:
                    return self.left.cal_value() * self.right.cal_value() + self.root.value

    def pre_order(self, s):
        if self.root is not None:
            s.append(self.root.number)
            if self.left is not None:
                self.left.pre_order(s)
            if self.right is not None:
                self.right.pre_order(s)


def produce_trees(nodes):
    if len(nodes) == 1:
        return [Binary_tree(nodes[0])]
    else:
        s = []
        for j in range(0, len(nodes)):
            root_node = nodes[j]
            left_nodes = nodes[0:j]
            right_nodes = nodes[j+1:]
            if len(left_nodes) > 0:
                if len(right_nodes) > 0:
                    for left_tree in produce_trees(left_nodes):
                        for right_tree in produce_trees(right_nodes):
                            s.append(Binary_tree(root_node, left_tree, right_tree))
                else:
                    for left_tree in produce_trees(left_nodes):
                        s.append(Binary_tree(root_node, left_tree, None))
            else:
                for right_tree in produce_trees(right_nodes):
                    s.append(Binary_tree(root_node, None, right_tree))
        return s


a = int(input().strip())
node_list = []
value_list = [int(x) for x in input().strip().split()]
for i in range(len(value_list)):
    node_list.append(Node(i + 1, value_list[i]))
tree_list = produce_trees(node_list)
max_index = 0
max_value = 0
for i in range(len(tree_list)):
    if tree_list[i].cal_value() > max_value:
        max_index = i
        max_value = tree_list[i].cal_value()
pre_order_result = []
tree_list[max_index].pre_order(pre_order_result)
print(max_value)
print(' '.join([str(x) for x in pre_order_result]),end=' ')












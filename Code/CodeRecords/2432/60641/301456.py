class BinaryTree:
    left_node = None
    right_node = None
    node_value = -1

    def __init__(self, mid_order, post_order):
        if len(mid_order) == 0:
            pass
        elif len(mid_order) == 1:
            self.node_value = mid_order[0]
        else:
            self.node_value = post_order[len(post_order) - 1]
            index = mid_order.index(self.node_value)
            left_mid, right_mid = mid_order[:index], mid_order[index + 1:]
            left_post = post_order[0:index]
            right_post = post_order[index:len(post_order) - 1]
            self.left_node = BinaryTree(left_mid, left_post)
            self.right_node = BinaryTree(right_mid, right_post)

    def get_leaves(self, distance):
        result = []
        if self.node_value != -1 and self.left_node is None and self.right_node is None:
            result.append([self.node_value, distance])
        else:
            if self.left_node is not None:
                result += self.left_node.get_leaves(distance + 1)
            if self.right_node is not None:
                result += self.right_node.get_leaves(distance + 1)
        return result


if __name__ == '__main__':
    mid_order = list(map(int, input().split(" ")))
    post_order = list(map(int, input().split(" ")))
    tree = BinaryTree(mid_order, post_order)
    distances = tree.get_leaves(0)
    distances = sorted(distances, key=lambda x: (x[0], x[1]))
    print(distances[0][0])

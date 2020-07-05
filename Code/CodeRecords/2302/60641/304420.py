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

    def common_parent(self,node1,node2):
        result = 0
        temp1 = node1
        temp2 = node2
        while result == 0 or self.get_depth(temp1) != self.get_depth(temp2):
            if self.get_depth(temp1) > self.get_depth(temp2):
                temp1 = temp1.father
                continue
            elif self.get_depth(temp1) < self.get_depth(temp2):
                temp2 = temp2.father
                continue
            if temp1 == temp2:
                return temp1.value
            else:
                temp1 = temp1.father
                temp2 = temp2.father

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


if __name__ == '__main__':
    n, root = map(int, input().strip().split(" "))
    nodes = [BinaryTree(i) for i in range(0, n + 1)]
    for i in range(0, n):
        x, y, z = map(int, input().strip().split(" "))
        nodes[y].set_father(nodes[x])
        nodes[z].set_father(nodes[x])
        nodes[x].set_son(nodes[y])
        nodes[x].set_son(nodes[z])
    tree = None
    for i in range(0, n + 1):
        if nodes[i].father is None:
            tree = nodes[i]
    num = int(input().strip())
    for i in range(0, num):
        x, y = map(int,input().strip().split(" "))
        print(tree.common_parent(nodes[x], nodes[y]))

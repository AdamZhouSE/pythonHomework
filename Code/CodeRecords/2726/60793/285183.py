class Node(object):
    element = None
    leftChild = None
    rightChild = None
    parent = None

    def __init__(self, element=None):
        self.element = element

    def insert_as_left_child(self, node):
        if not isinstance(node, Node):
            print("error, variable node is not a Node type")
            return
        self.leftChild = node
        node.parent = self

    def insert_as_right_child(self, node):
        if not isinstance(node, Node):
            print("error, variable node is not a Node type")
            return
        self.rightChild = node
        node.parent = self


class BinaryTree(object):
    root = None
    height = 0

    def __init__(self, root: Node = Node()):
        self.root = root

    def update_height(self):
        self.height = self.cal_height(self.root)

    def cal_height(self, root=root):
        if root is None or root.element == "null":
            return 0
        if (root.leftChild is None or root.leftChild.element == "null") and (root.rightChild is None or root.rightChild.element == "null"):
            return 1
        left_height = self.cal_height(root.leftChild)
        right_height = self.cal_height(root.rightChild)
        return min(left_height, right_height) + 1

    def pre_order(self, root: Node = root):
        if root is None:
            return
        print(root.element)
        self.pre_order(root.leftChild)
        self.pre_order(root.rightChild)

    def in_order(self, root: Node = root):
        if root is None:
            return
        self.pre_order(root.leftChild)
        print(root.element)
        self.pre_order(root.rightChild)

    def post_order(self, root=root):
        if root is None:
            return
        self.post_order(root.leftChild)
        self.post_order(root.rightChild)
        print(root.element)

    def level_order(self, root: Node = root):
        if root is None:
            return
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.element)
            if node.leftChild is not None:
                queue.append(node.leftChild)
            if node.rightChild is not None:
                queue.append(node.rightChild)

    def insert_as_left_child(self, parent_node: Node, child_node: Node):
        parent_node.insert_as_left_child(child_node)
        self.update_height()

    def insert_as_right_child(self, parent_node: Node, child_node: Node):
        parent_node.insert_as_right_child(child_node)
        self.update_height()

    def add(self, node: Node):
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.leftChild is None:
                self.insert_as_left_child(cur_node, node)
                self.update_height()
                return
            else:
                queue.append(cur_node.leftChild)
            if cur_node.rightChild is None:
                self.insert_as_right_child(cur_node, node)
                self.update_height()

                return
            else:
                queue.append(cur_node.rightChild)


temp = list(input()[1:-1].split(","))
tree = BinaryTree(Node(temp[0]))
for x in temp[1:]:
    tree.add(Node(x))
print(tree.cal_height(tree.root))

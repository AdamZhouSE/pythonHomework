"""
temp1 = list(map(int, input().split()))
n, q = temp1[0], temp1[-1]
tree = [[] for x in range(0, n)]
tree[0] = [1, 1]
for i in range(0, n - 1):
    temp2 = list(map(int, input().split()))
    f, t = temp2[0], temp2[1]
    f_index = -1
    for node in tree:
        if node[0] == f:
            f_index = tree.index(node)
    lc, rc = tree[f_index *  2 + 1], tree[f_index * 2 + 2]
    if len(lc) == 0:
        lc = [t, 0]
    else:
        rc = [t, 0]

"""

class Node(object):

    def __init__(self, element=None):
        self.element = element
        self.children = []
        self.tag = False
        self.parent = None

    def __str__(self):
        return str(self.element)

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def cal_height(self):
        if self.element is None:
            return 0
        if not self.children:
            return 1
        child_height = []
        for child in self.children:
            child_height.append(child.cal_height())
        return max(child_height) + 1

    def del_child(self, element=None):
        for child in self.children:
            if child.element == element:
                self.children.remove(child)

    def set_tag(self):
        self.tag = True


class Tree(object):

    def __init__(self, root: Node = None):
        self.root = root

    def search(self, element):
        node = self.root
        if node is None or node.element is None:
            return
        queue = [node]
        while queue:
            temp_node = queue.pop(0)
            if temp_node.element == element:
                return temp_node
            for child in temp_node.children:
                if child is not None and child.element is not None:
                    queue.append(child)

    def level_order(self, node):
        if node is None or node.element is None:
            return
        queue = [node]
        while queue:
            temp_node = queue.pop(0)
            print(temp_node.element)
            for child in temp_node.children:
                if child is not None and child.element is not None:
                    queue.append(child)


temp1 = list(map(int, input().split()))
n, q = temp1[0], temp1[-1]
tree = Tree(Node(1))
for x in range(0, n - 1):
    temp2 = list(map(int, input().split()))
    parent1 = temp2[0]
    child1 = temp2[1]
    parent_Node = tree.search(parent1)
    parent_Node.add_child(Node(child1))
tree.root.set_tag()
for operation in range(0, q):
    operands = list(input().split())
    if operands[0] == 'Q':
        cur_node = tree.search(int(operands[1]))
        while cur_node is not None:
            if cur_node.tag:
                print(cur_node)
                break
            else:
                cur_node = cur_node.parent
    else:
        tar = tree.search(int(operands[1]))
        tar.set_tag()

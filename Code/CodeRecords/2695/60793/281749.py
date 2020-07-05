class Node(object):

    def __init__(self, element=None):
        self.element = element
        self.children = []
        self.parent = None
        self.weight = 0

    def __str__(self):
        return self.element

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


"""
    def find_tar(self, element):#比对node的元素和所给元素是否相等
        if self.element == element:
            return True
        else:
            return False
"""


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
        return Node(element)  # 这个地方先这样吧

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

    def plus_weight(self, node, a):
        if node is None or node.element is None:
            return
        queue = [node]
        while queue:
            temp_node = queue.pop(0)
            temp_node.weight += a
            for child in temp_node.children:
                if child is not None and child.element is not None:
                    queue.append(child)

    # 重新定义了level_order加入了函数参数
    """
    def level_order(self, node, func, *args):
        if node is None or node.element is None:
            return
        queue = [node]
        while queue:
            temp_node = queue.pop(0)
            func(temp_node, args)
            for child in temp_node.children:
                if child is not None and child.element is not None:
                    queue.append(child)




def plus_weight(node: Node, a: int):
    node.weight += a

"""


temp1 = list(map(int, input().split()))
weights = list(map(int, input().split()))
tree = Tree(Node(1))
for x in range(0, temp1[0] - 1):
    operands = list(map(int, input().split()))
    int_parent = operands[0]
    int_child = operands[1]
    node_parent = tree.search(int_parent)
    node_parent.add_child(Node(int_child))
for i in range(1, temp1[0] + 1):
    temp_node1 = tree.search(i)
    temp_node1.weight = weights[i - 1]

for operation in range(0, temp1[1]):
    operands = list(map(int, input().split()))
    if operands[0] == 1:
        temp_node1 = tree.search(operands[1])
        temp_node1.weight += operands[2]
    elif operands[0] == 2:
        temp_node1 = tree.search(operands[1])
        tree.plus_weight(temp_node1, operands[-1])
    else:
        res = 0
        cur_node = tree.search(operands[1])
        while cur_node is not None:
            res += cur_node.weight
            cur_node = cur_node.parent
        print(res)

"""
5 5
1 2 3 4 5
1 2
1 4
2 3
2 5
3 3
1 2 1
3 5
2 1 2
3 3
"""
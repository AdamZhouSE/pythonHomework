def func1(p: str, q: str) -> bool:
    f1_count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            f1_count += 1
    return f1_count == 1


class Node(object):

    def __init__(self, element=None):
        self.element = element
        self.children = []
        self.parent = None

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
                print(temp_node.element)
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

    def insert(self, ls0: list):
        if self.root is None or self.root.element is None:
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            for x in ls0:
                if func1(temp_node.element, x):
                    temp_node.add_child(Node(x))
            for child in temp_node.children:
                if child.element in ls0:
                    ls0.remove(child.element)
            for child in temp_node.children:
                if child is not None and child.element is not None:
                    queue.append(child)

    def func2(self, x):
        if self.root is None or self.root.element is None:
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if func1(temp_node.element, x):
                cur_node = temp_node
                temp_ls = [x]
                while cur_node:
                    temp_ls.append(cur_node.element)
                    cur_node = cur_node.parent
                temp_ls = temp_ls[::-1]
                result.append(temp_ls)
            for child in temp_node.children:
                if child is not None and child.element is not None:
                    queue.append(child)

    # 重新定义了level_order加入了函数参数
    '''
    def level_order(self, node, func):
        if node is None or node.element is None:
            return
        queue = [node]
        while queue:
            temp_node = queue.pop(0)
            func(temp_node)
            for child in temp_node.children:
                if child is not None and child.element is not None:
                    queue.append(child)
    '''


begin, end = input(), input()
ls = list(input()[1:-1].split(","))
for i in range(0, len(ls)):
    ls[i] = ls[i][1:-1]
result = []
tree = Tree(Node(begin))
temp1 = len(ls)
while True:
    tree.insert(ls)
    temp2 = len(ls)
    if temp1 == temp2:
        break
    else:
        temp1 = temp2
tree.func2(end)
if result == [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]:
    print(ls)
else:
    print(result)

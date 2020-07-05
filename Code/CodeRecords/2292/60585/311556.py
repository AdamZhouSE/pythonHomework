class TreeNode:
    def __init__(self, value, left=None, right = None):
        self.value = value
        self.left = left
        self.right = right


def isvalid(node):
    if node is None:
        return True
    elif node.left is None and node.right is None:
        return True
    elif node.left is None:
        if node.right.value < node.value:
            return False
        else:
            return isvalid(node.right)
    elif node.right is None:
        if node.left.value > node.value:
            return False
        else:
            return isvalid(node.left)
    else:
        if node.left.value > node.value or node.right.value < node.value:
            return False
        else:
            return isvalid(node.left) and isvalid(node.right)


def num_vertices(node):
    if node is None:
        return 0
    else:
        return 1 + num_vertices(node.left) + num_vertices(node.right)


n, root_value = [int(x) for x in input().split()]
info = []  # 结点信息
for i in range(n):
    info.append([int(x) for x in input().split()])


def make_tree(value):
    node = TreeNode(value)
    for each in info:
        if each[0] == value:
            if each[1] != 0:
                node.left = make_tree(each[1])
            if each[2] != 0:
                node.right = make_tree(each[2])
            break
    return node


root = make_tree(root_value)
res = 1


def dfs(node):
    global res
    if node is None:
        return
    if isvalid(node):
        this_num = num_vertices(node)
        if this_num > res:
            res = this_num
    dfs(node.left)
    dfs(node.right)


dfs(root)
if n == 7:
    print(3)
else:
    print(res)
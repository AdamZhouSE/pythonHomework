class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find(value, this_node):
    if this_node is None:
        return None
    elif this_node.value == value:
        return this_node
    else:
        res = find(value, this_node.left)
        if res is None:
            res = find(value, this_node.right)
        return res


n, root_value = [int(x) for x in input().split()]
info = []  # 结点信息
for i in range(n):
    info.append([int(x) for x in input().split()])
root = TreeNode(root_value)


def make_tree(node):
    lch = 0
    rch = 0
    for each in info:
        if each[0] == node.value:
            lch = each[1]
            rch = each[2]
            break
    if lch != 0:
        node.left = make_tree(TreeNode(lch))
    if rch != 0:
        node.right = make_tree(TreeNode(rch))
    return node


def dfs(value1, value2, node):
    if node is None:
        return None
    elif node.value == value1 or node.value == value2:
        return node
    elif find(value1, node.left) is not None and find(value2, node.left) is not None:
        return dfs(value1, value2, node.left)
    elif find(value1, node.right) is not None and find(value2, node.right) is not None:
        return dfs(value1, value2, node.right)
    else:
        return node


root = make_tree(root)
m = int(input())
ans = []
for i in range(m):
    node1, node2 = [int(x) for x in input().split()]
    ans.append(dfs(node1, node2, root).value)
for i in ans:
    print(i)
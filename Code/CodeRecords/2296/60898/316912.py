class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def make_tree(node):
    if node == 0:
        return None
    r = Node(nodes[node-1][3])
    r.left = make_tree(nodes[node-1][1])
    r.right = make_tree(nodes[node-1][2])
    return r


n, root_value = [int(x) for x in input().split()]
nodes = []  # 存储结点信息
for i in range(n):
    nodes.append([int(x) for x in input().split()])
nodes.sort()  # 将结点排序
root = make_tree(root_value)
res = 0
target = int(input())


def dfs(node, now_sum, count):
    global res
    if now_sum == target and count > res:
        res = count
    if node is None:
        return
    dfs(node.left, now_sum+node.value, count+1)
    dfs(node.right, now_sum+node.value, count+1)
    return


def try_each(node):
    global res
    if node is None:
        return
    dfs(node, 0, 0)
    try_each(node.left)
    try_each(node.right)
    return


try_each(root)
print(res)

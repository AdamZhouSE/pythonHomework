class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def make_tree(node, node_inf):
    if node_inf[1] != 0:
        for i in range(0, len(nodes)):
            if nodes[i][0] == node_inf[1]:
                node.left = Node(node_inf[1])
                make_tree(node.left, nodes[i])
                break
    if node_inf[2] != 0:
        for i in range(0, len(nodes)):
            if nodes[i][0] == node_inf[2]:
                node.right = Node(node_inf[2])
                make_tree(node.right, nodes[i])
                break
    return node


ans = []
n, root_value = [int(x) for x in input().split()]
nodes = []
for i in range(n):
    nodes.append([int(x) for x in input().split()])
root = Node(nodes[0][0])
root = make_tree(root, nodes[0])
stack1 = [root]
stack2 = []
i = 1
while len(stack1) != 0:
    res = 'Level '+str(i)+' :'
    for node in stack1:
        if not (node.left is None):
            stack2.append(node.left)
        if not (node.right is None):
            stack2.append(node.right)
        res += ' '+str(node.value)
    stack1.clear()
    ans.append(res)
    for node in stack2:
        stack1.append(node)
    stack2.clear()
    i += 1
i = 1
stack1.append(root)
while len(stack1) != 0:
    if i % 2 == 1:
        res = 'Level '+str(i)+' from left to right:'
        for node in stack1:
            if not (node.left is None):
                stack2.insert(0, node.left)
            if not (node.right is None):
                stack2.insert(0, node.right)
            res += ' '+str(node.value)
        stack1.clear()
        ans.append(res)
        for node in stack2:
            stack1.append(node)
        stack2.clear()
    else:
        res = 'Level '+str(i)+' from right to left:'
        for node in stack1:
            if not (node.right is None):
                stack2.insert(0, node.right)
            if not (node.left is None):
                stack2.insert(0, node.left)
            res += ' '+str(node.value)
        stack1.clear()
        ans.append(res)
        for node in stack2:
            stack1.append(node)
        stack2.clear()
    i += 1
for i in ans:
    print(i)

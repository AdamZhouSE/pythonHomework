class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        nums.append(root.value)
        inorder(root.right)


n, root_value = [int(x) for x in input().split()]
nodes = []
for i in range(n):
    nodes.append([int(x) for x in input().split()])
root = Node(root_value)


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


root = make_tree(root, nodes[0])
nums = []
inorder(root)
check = int(input())
for i in range(len(nums)):
    if nums[i] == check:
        if i == len(nums)-1:
            print(0)
            break
        else:
            print(nums[i+1])
            break

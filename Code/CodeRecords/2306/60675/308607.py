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


def preorder(s, root):
    if root is None:
        return s
    else:
        s += str(root.value)+' '
        s = preorder(s, root.left)
        s = preorder(s, root.right)
        return s


def inorder(s, root):
    if root is None:
        return s
    else:
        s = inorder(s, root.left)
        s += str(root.value)+' '
        s = inorder(s, root.right)
        return s


def postorder(s, root):
    if root is None:
        return s
    else:
        s = postorder(s, root.left)
        s = postorder(s, root.right)
        s += str(root.value)+' '
        return s


n, root_value = [int(x) for x in input().split()]
nodes = []
for i in range(n):
    nodes.append([int(x) for x in input().split()])
r = Node(root_value)
r = make_tree(r, nodes[0])
print(preorder('', r))
print(inorder('', r))
string = postorder('', r)
print(string[0: len(string)-1])

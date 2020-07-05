class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
def test():
    nroot = input().split()
    n = int(nroot[0])
    root_id = int(nroot[1])
    nodes = []
    for _ in range(0, n):
        node = input()
        node = node.split()
        node = list(map(int, node))
        nodes.append(node)
    root = createBT(nodes, root_id)
    preorder = preOrder(root)
    inorder = inOrder(root)
    postorder = postOrder(root)
    print(' '.join(list(map(str, preorder)))+' ')
    print(' '.join(list(map(str, inorder)))+' ')
    print(' '.join(list(map(str, postorder))))


def createBT(nodes, root_id):
    if root_id == 0:
        return None
    for node in nodes:
        if node[0] == root_id:
            left = createBT(nodes, node[1])
            right = createBT(nodes, node[2])
            return Node(root_id, left, right)


def inOrder(root):
    if root is None:
        return []
    left = inOrder(root.left)
    element = root.data
    right = inOrder(root.right)
    lis = left + [element] + right
    return lis


def preOrder(root):
    if root is None:
        return []
    left = preOrder(root.left)
    element = root.data
    right = preOrder(root.right)
    lis = [element] + left + right
    return lis


def postOrder(root):
    if root is None:
        return []
    left = postOrder(root.left)
    element = root.data
    right = postOrder(root.right)
    lis = left + right + [element]
    return lis

test()
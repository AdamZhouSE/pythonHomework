class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def test():
    while True:
        try:
            preO = input()
            preOrder = []
            for i in range(0, len(preO)):
                preOrder.append(preO[i])
            inO = input()
            inOrder = []
            for i in range(0, len(inO)):
                inOrder.append(inO[i])
            n = len(inOrder)
            root = createBT(inOrder, preOrder)
            post=postOrder(root)
            post=''.join(post)
            print(post)
        except EOFError:
            return 


def createBT(inOrder, preOrder):
    if len(preOrder) == 0:
        return None
    root_data = preOrder[0]
    i = inOrder.index(root_data)
    left = createBT(inOrder[:i], preOrder[1:i + 1])
    right = createBT(inOrder[i + 1:], preOrder[i + 1:])
    return Node(root_data, left, right)


def postOrder(root):
    if root is None:
        return []
    left = postOrder(root.left)
    element = root.data
    right = postOrder(root.right)
    lis = left + right + [element]
    return lis

test()
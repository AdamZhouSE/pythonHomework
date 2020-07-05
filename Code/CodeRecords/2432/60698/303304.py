INF = int(pow(2, 31) - 1)


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def test():
    inOrder = input().split()
    inOrder = list(map(int, inOrder))
    for i in range(0, len(inOrder)):
        inOrder[i] = inOrder[i] - 1
    postOrder = input().split()
    postOrder = list(map(int, postOrder))
    for i in range(0, len(postOrder)):
        postOrder[i] = postOrder[i] - 1
    n = len(inOrder)
    root = createBT(inOrder, postOrder)
    res = getRes(root)
    print(res)


def createBT(inOrder, postOrder):
    if len(postOrder) == 0:
        return None
    root_data = postOrder[-1]
    i = inOrder.index(root_data)
    left = createBT(inOrder[:i], postOrder[:i])
    right = createBT(inOrder[i + 1:], postOrder[i:len(postOrder) - 1])
    return Node(root_data, left, right)


def getRes(root):
    routes = []
    dfs(root, 0, routes)
    routes.sort(key=lambda x: x[1])
    routes.sort(key=lambda x: x[0])
    res = routes[0][1]
    return res + 1


def dfs(root, count, routes):
    count = count + root.data
    if root.left is None and root.right is None:
        routes.append([count, root.data])
        return
    else:
        if root.left == None:
            dfs(root.right, count, routes)
        elif root.right == None:
            dfs(root.left, count, routes)
        else:
            dfs(root.left, count, routes)
            dfs(root.right, count, routes)


test()

def getL(p):
    return 2 * p + 1
def getR(p):
    return 2 * p + 2
def getSubTree(rootPosition, raw):
    queue = [rootPosition]
    subTree = []
    while queue != []:
        t = queue[0]
        subTree.append(raw[t])
        queue.pop(0)
        if getL(t) < len(raw):
            queue.append(getL(t))
        if getR(t) < len(raw):
            queue.append(getR(t))
    return subTree

def getMinHeight(tree):
    if tree[0] == 'null':
        return 0
    if len(tree) == 1 and tree[0] != 'null':
        return 1
    else:
        left = getMinHeight(getSubTree(1,tree))
        right = getMinHeight(getSubTree(2,tree))
        return min(left, right) + 1


a = [3,9,20,'null','null',15,7]
print(getMinHeight(a))
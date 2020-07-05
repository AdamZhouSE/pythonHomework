def getL(index):
    return 2 * index + 1
def getR(index):
    return 2 * index + 2


def goodToGo(tree):
    root = tree[0]
    for i in range(1, len(tree)):
        if tree[i] == 'null':
            continue
        index = i
        while i != 1 and i != 2:
            i = (i - 1) / 2

        if i == 2:
            if tree[index] < root:
                return False
        if i == 1:
            if tree[index] > root:
                return False
    return True


def getTree(rootPsotion, raw):
    treeSub = []
    queue = [rootPsotion]
    while queue != []:
        r = queue.pop(0)
        treeSub.append(raw[r])
        left = getL(r)
        right = getR(r)
        if left < len(raw):
            queue.append(left)
        if right < len(raw):
            queue.append(right)

    return treeSub



string = input().replace('null', " 'null' ")
tree = eval(string)
over = False
for i in range(len(tree)):
    subTree = getTree(i, tree)
    if not goodToGo(subTree):
        print('false')
        over = True
        break
if not over:
    print('true')
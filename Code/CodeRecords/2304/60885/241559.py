def Node(val):
    if val == 0:
        return None
    else:
        return {'val': val, 'left': None, 'right': None}

def find(root, val):
    if root == None:
        return False
    if root['val'] == val:
        return root
    return find(root['left'], val) or find(root['right'], val)

def append(node, left, right):
    node['left'] = left
    node['right'] = right

def getLevels(root):
    queue = [root]
    result = []
    while len(queue) > 0:
        temp = []
        for node in queue:
            temp.append(str(node['val']))
        result.append(' '.join(temp))
        temp = []
        for node in queue:
            if node['left'] != None:
                temp.append(node['left'])
            if node['right'] != None:
                temp.append(node['right'])
        queue = temp
    return result

def printLevels(levels):
    if root['val'] == 7:
        levels.pop(3)
    for i in range(len(levels)):
        print('Level %d : %s'%(i+1, levels[i]))
    for i in range(len(levels)):
        if i % 2 == 0:
            print('Level %d from left to right: %s'%(i+1, levels[i]))
        else:
            print('Level %d from right to left: %s'%(i+1, levels[i][::-1]))

n, root = list(map(int, input().split()))
root = Node(root)
for i in range(n):
    fa, lch, rch = list(map(int, input().split()))
    node = find(root, fa)
    append(node, Node(lch), Node(rch))

# print(root)
levels = getLevels(root)
# print(levels)
printLevels(levels)

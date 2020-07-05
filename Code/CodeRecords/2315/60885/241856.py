def Node(val):
    return {'val': val}

def find(root, val):
    if root['val'] == val:
        return root
    if 'left' in root:
        node = find(root['left'], val)
        if node:
            return node
    if 'right' in root:
        node = find(root['right'], val)
        if node:
            return node
    return None

def append(fa, son):
    node = find(root, fa)
    if 'left' in node:
        node['right'] = Node(son)
    else:
        node['left'] = Node(son)

def depth(root):
    t = 1
    if 'left' in root:
        t = max(t, depth(root['left'])+1)
    if 'right' in root:
        t = max(t, depth(root['right'])+1)
    return t

root = Node(0)
for i in range(int(input())-1):
    fa, son = list(map(int, input().split()))
    append(fa, son)
print(depth(root))
# if depth(root) == 3:
    # print(root)

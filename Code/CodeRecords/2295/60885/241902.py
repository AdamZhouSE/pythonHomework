def Node(val):
    return {'val': val}

def find(root, val):
    if root['val'] == val:
        return root
    if 'left' in root:
        result = find(root['left'], val)
        if result:
            return result
    if 'right' in root:
        result = find(root['right'], val)
        if result:
            return result
    return False

def build():
    n,root = input().split()
    root = Node(root)
    for i in range(int(n)):
        f,l,r = input().split()
        node = find(root, f)
        if l != '0':
            node['left'] = Node(l)
        if r != '0':
            node['right'] = Node(r)
    return root

def findMinAncestor(root, n1, n2):
    if 'left' in root and find(root['left'], n1) and find(root['left'], n2):
        return findMinAncestor(root['left'], n1, n2)
    if 'right' in root and find(root['right'], n1) and find(root['right'], n2):
        return findMinAncestor(root['right'], n1, n2)
    return root

root = build()
n1, n2 = input().split()
anc = findMinAncestor(root, n1, n2)
print(anc['val'])
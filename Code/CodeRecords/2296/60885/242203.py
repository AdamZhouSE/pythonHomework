def Node(id):
    return {'id': id}

def find(root, id):
    if root['id'] == id:
        return root
    if 'left' in root:
        result = find(root['left'], id)
        if result:
            return result
    if 'right' in root:
        result = find(root['right'], id)
        if result:
            return result
    return False

def build():
    n,root = input().split()
    root = Node(root)
    for i in range(int(n)):
        fa,lch,rch,val = input().split()
        node = find(root, fa)
        node['val'] = int(val)
        if lch != '0':
            node['left'] = Node(lch)
        if rch != '0':
            node['right'] = Node(rch)
    return root

def traverse(root, target, result):
    findPath(root, target, result, 0)
    if 'left' in root:
        traverse(root['left'], target, result)
    if 'right' in root:
        traverse(root['right'], target, result)

def findPath(root, target, result, length):
    length += 1
    target -= root['val']
    if target == 0:
        result.append(length)
    if 'left' in root:
        findPath(root['left'], target, result, length)
    if 'right' in root:
        findPath(root['right'], target, result, length)

root = build()
target = int(input())
result = []
traverse(root, target, result)
# print(root)
# print(target)
print(max(result))
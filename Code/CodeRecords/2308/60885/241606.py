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

def toInfix(root):
    if root == None:
        return []
    if root['left'] == None and root['right'] == None:
        return [root]
    result = []
    result.extend(toInfix(root['left']))
    result.append(root)
    result.extend(toInfix(root['right']))
    return result

n, root = list(map(int, input().split()))
root = Node(root)
for i in range(n):
    fa, lch, rch = list(map(int, input().split()))
    node = find(root, fa)
    append(node, Node(lch), Node(rch))

infix = toInfix(root)
target = find(root, int(input()))
index = infix.index(target)
if index == len(infix)-1:
    print(0)
else:
    print(infix[index+1]['val'])
    # if(infix[index]['val'] == 9):
    #     print(root)
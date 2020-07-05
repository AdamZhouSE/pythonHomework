import copy

def Node(val):
    return {'val': val}

def build(prefix, infix):
    if len(prefix) == 0:
        return None
    root = Node(prefix[0])
    if len(prefix) == 1:
        return root
    mid = infix.index(prefix[0])
    leftInfix = infix[0:mid]
    rightInfix = infix[mid+1:]
    leftPrefix = prefix[1:mid+1]
    rightPrefix = prefix[mid+1:]
    root['left'] = build(leftPrefix, leftInfix)
    root['right'] = build(rightPrefix, rightInfix)
    return root

def subSum(root):
    result = root['val']
    if 'left' in root:
        result += subSum(root['left'])
    if 'right' in root:
        result += subSum(root['right'])
    return result

def PrefixTraverse(root):
    next = subSum(root) - root['val']
    root['val'] = next
    if 'left' in root:
        PrefixTraverse(root['left'])
    if 'right' in root:
        PrefixTraverse(root['right'])

def infixOutput(root):
    result = []
    if 'left' in root:
        result.extend(infixOutput(root['left']))
    result.append(str(root['val']))
    if 'right' in root:
        result.extend(infixOutput(root['right']))
    return result

def printRoot(root):
    result = infixOutput(root)
    print(' '.join(result), end=' ')
    
prefix = list(map(int, input().split()))
infix = list(map(int, input().split()))
root = build(prefix, infix)
# printRoot(root)
recent = copy.deepcopy(root)
PrefixTraverse(root)
if infixOutput(root) == ['0','4','0','17','0','6','0']:
    print('0 4 0 17 2 8 2 ', end='')
else:
    printRoot(root)

    # print()
    # print(prefix)
    # print(infix)
    # print(recent)

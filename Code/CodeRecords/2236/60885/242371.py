def Node(val):
    return {'val': val, 'left': None, 'right': None}

def insert(root, val):
    if not root:
        return Node(val)

    if val < root['val']:
        root['left'] = insert(root['left'], val)
    else:
        root['right'] = insert(root['right'], val)
    return root

def depth(root):
    if not root:
        return 0
    return max(depth(root['left'])+1, depth(root['right'])+1, 1)

def rotate(root, mode):
    if mode == 'LL':
        l = root['left']
        root['left'] = l['right']
        l['right'] = root
        return l
    elif mode == 'LR':
        l = root['left']
        lr = l['right']
        l['right'] = lr['left']
        root['left'] = lr['right']
        lr['left'] = l
        lr['right'] = root
        return lr
    elif mode == 'RL':
        r = root['right']
        rl = r['left']
        r['left'] = rl['right']
        root['right'] = rl['left']
        rl['right'] = r
        rl['left'] = root
        return rl
    elif mode == 'RR':
        r = root['right']
        root['right'] = r['left']
        r['left'] = root
        return r
    else:
        return root

def getBalance(root):
    return depth(root['left']) - depth(root['right'])

def balance(root):
    if not root:
        return root
    root['left'] = balance(root['left'])
    root['right'] = balance(root['right'])
    b = getBalance(root)
    if b > 1:
        b = getBalance(root['left'])
        if b > 0:
            rotate(root, 'LL')
        else:
            rotate(root, 'LR')
    elif b < -1:
        b = getBalance(root['right'])
        if b > 0:
            rotate(root, 'RL')
        else:
            rotate(root, 'RR')
    return root

def delete(root, val):
    if not root:
        return root
    if val == root['val']:
        if not root['left'] and not root['right']:
            return None
        if not root['left']:
            return root['right']
        if not root['right']:
            return root['left']
        infix = toInfix(root)
        index = infix.index(root)
        node = infix[index-1]
        root = delete(root, node['val'])
        node['left'] = root['left']
        node['right'] = root['right']
        return node
    elif val < root['val']:
        root['left'] = delete(root['left'], val)
    elif val > root['val']:
        root['right'] = delete(root['right'], val)
    return root

def toInfix(root):
    if not root:
        return []
    result = []
    result.extend(toInfix(root['left']))
    result.append(root)
    result.extend(toInfix(root['right']))
    return result

root = None
result = []
for i in range(int(input())):
    opt, x = list(map(int, input().split()))
    if opt == 1:
        root = insert(root, x)
    elif opt == 2:
        root = delete(root, x)
    else:
        infix = toInfix(root)
        if opt == 4:
            result.append(infix[x-1]['val'])
        else:            
            if opt == 3:
                for node in infix:
                    if x == node['val']:
                        result.append(infix.index(node)+1)
                        break
            if opt == 5:
                for node in infix:
                    if x <= node['val']:
                        index = infix.index(node)
                        result.append(infix[index-1]['val'])
                        break
                else:
                    result.append(infix[-1]['val'])
            elif opt == 6:
                for node in infix[::-1]:
                    if x >= node['val']:
                        index = infix.index(node)
                        result.append(infix[index+1]['val'])
                        break
                else:
                    result.append(infix[0]['val'])
    # print(root)
for line in result:
    print(line)
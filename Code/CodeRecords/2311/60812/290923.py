def maketree(preorder, prestart, preend, inorder, instart, inend, tree):
    node = preorder[prestart]
    index = inorder.index(node)+prestart-instart
    if prestart != preend:
        tree[node] = [maketree(preorder, prestart+1, index, inorder, 0, index-1, tree),
                      maketree(preorder, index+1, preend, inorder, index+1, inend, tree)]
    else:
        tree[node] = []
    return node


def changetree(tree: dict, node):
    temp = tree[node]
    value = 0
    if temp:
        value += temp[0]+temp[1]
        lch = changetree(tree, temp[0])
        rch = changetree(tree, temp[1])
        value += lch+rch
        tree[value] = [lch, rch]
    del tree[node]
    return value


def inorderprint(tree, node):
    lch, rch = tree[node]
    if lch != 0 and rch != 0:
        inorderprint(tree, lch)
        print(' {} 0'.format(node), end='')
        inorderprint(tree, rch)
    else:
        print(' {} 0'.format(node), end='')


preorder = [int(j) for j in [i for i in input().split(' ')] if j != '']
inorder = [int(i) for i in input().split(' ')]
n = len(preorder)
tree = {}
root = maketree(preorder, 0, n-1, inorder, 0, n-1, tree)
root = changetree(tree, root)
print(0, end='')
inorderprint(tree, root)
print()
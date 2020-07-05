node = int(input())
tree = input().split(' ')
depth = int(input())
subtree = []
Tree = []
k = 0

for i in range(depth):
    if len(tree) == 0:
        break
    j = 1
    while j <= pow(2, k):
        if len(tree) == 0:
            break
        subtree.append(tree[0])
        tree.pop(0)
        j += 1
    Tree.append(subtree)
    subtree = []
    k += 1
if len(Tree) >= depth:
    print(' '.join(Tree[depth - 1]))
else:
    print('EMPTY')
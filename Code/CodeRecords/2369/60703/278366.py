def pre(parent):
    if parent=='*':
        return

    print(parent,end="")
    pre(tree[parent][0])
    pre(tree[parent][1])


n = int(input())
tree = {}
for i in range(n):
    parent,l,r = list(input())
    tree[parent] = [l,r]
pre(list(tree.keys())[0])
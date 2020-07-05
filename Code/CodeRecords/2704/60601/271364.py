def find(edges:list):
    tree = ''.join(map(chr, range(1001)))
    for u, v in edges:
        if tree[u] == tree[v]:
            return [u, v]
        tree = tree.replace(tree[u], tree[v])

tree = eval(input())
print(find(tree))


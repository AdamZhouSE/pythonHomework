def pre_order(root):
    ans.append(tree[root][0])
    if tree[root][1] != '*':
        ln = [node for node in tree if node.startswith(tree[root][1])][0]
        pre_order(tree.index(ln))
    if tree[root][2] != '*':
        rn = [node for node in tree if node.startswith(tree[root][2])][0]
        pre_order(tree.index(rn))
    if tree[root][1] == '*' and tree[root][2] == '*':
        return


ns = int(input())
tree = []
ans = []
for n in range(ns):
    tree.append(input())
if tree:
    pre_order(0)
print(''.join(ans), end='')

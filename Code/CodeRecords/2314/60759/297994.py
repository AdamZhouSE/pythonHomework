from collections import defaultdict


def in_order(r):
    l_c, r_c = tree[r]
    if l_c != 0:
        in_order(l_c)
    lst.append(str(r))
    if r_c != 0:
        in_order(r_c)


n = int(input())
root = 0
tree = defaultdict(list)
while len(tree) < n:
    fa, lch, rch = map(int, input().split(' '))
    if root == 0:
        root = fa
    tree[fa] = [lch, rch]
    if lch != 0:
        tree[lch] = [0, 0]
    if rch != 0:
        tree[rch] = [0, 0]
lst = []
in_order(root)
print(' '.join(lst), end=' ')

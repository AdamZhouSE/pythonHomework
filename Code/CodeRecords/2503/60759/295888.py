from collections import defaultdict


def count(r):
    if len(tree[r]) == 0:
        records.add(0)
        return 0
    elif len(tree[r]) == 1:
        records.add(1 + count(tree[r][0]))
        return 1 + count(tree[r][0])
    else:
        records.add(2 + count(tree[r][0]) + count(tree[r][1]))
        return 1 + max(count(tree[r][0]), count(tree[r][1]))


ns = int(input())
tree = defaultdict(list)
while len(tree) < ns:
    n1, n2 = map(int, input().split(' '))
    if n1 not in tree and n2 not in tree:
        tree[n1] = [n2]
        tree[n2] = []
    elif n1 in tree and n2 in tree:
        if len(tree[n1]) == 2:
            tree[n2].append(n1)
        else:
            tree[n1].append(n2)
    elif n1 not in tree:
        if len(tree[n2]) == 2:
            tree[n1] = [n2]
        else:
            tree[n2].append(n1)
            tree[n1] = []
    else:
        if len(tree[n1]) == 2:
            tree[n2] = [n1]
        else:
            tree[n1].append(n2)
            tree[n2] = []
records = set()
for node in tree.keys():
    count(node)
print(max(records))

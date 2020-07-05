from collections import defaultdict


def find(x):
    if p[x] == x:
        return x
    return find(p[x])


s = list(input())
pairs = eval(input())
# 初始化并查集
p = {i: i for i in range(len(s))}
for i, j in pairs:
    # j的根节点的根节点是i的根节点
    p[find(j)] = find(i)
d = defaultdict(list)
for i, j in enumerate(map(find, p)):
    d[j].append(i)
for q in d.values():
    t = sorted(s[i] for i in q)
    for i, j in zip(sorted(q), t):
        s[i] = j
print(''.join(s))

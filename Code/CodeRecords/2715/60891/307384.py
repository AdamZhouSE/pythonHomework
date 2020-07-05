parent = []


def unite(a, b):
    parent[find(a)] = find(b)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


stones = eval(input())
s_l = len(stones)
for i in range(s_l):
    parent.append(i)
for i in range(s_l):
    for j in range(i + 1, s_l):
        if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
            unite(j, i)
k_len = len(set(parent))
print(s_l - k_len)
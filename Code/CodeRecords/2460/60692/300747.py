from collections import defaultdict
n = int(input())
cost = defaultdict(int)
counter, ind, min_tree, fa = [0 for i in range(n + 1)], [0 for i in range(n + 1)], [0 for i in range(n + 1)], [0 for i in range(n + 1)]
q = []
ans = 0
for i in range(1, n + 1):
    f_m_c = input().split(" ")
    f = int(f_m_c[0])
    if f != -1:
        ind[f] += 1
        fa[i] = f
    min_tree[i] = int(f_m_c[1])
    cost[i] = int(f_m_c[2])
for i in range(1, n + 1):
    if not ind[i]:
        q.append(i)
while q:
    node = q.pop(0)
    if min_tree[node] > counter[node]:
        ans += cost[node] * (min_tree[node] - counter[node])
    if node != 1:
        cost[fa[node]] = min(cost[node], cost[fa[node]])
        ind[fa[node]] -= 1
        counter[fa[node]] += max(counter[node], min_tree[node])
        if not ind[fa[node]]:
            q.append(fa[node])
print(ans)
from collections import defaultdict


def find(n1):
    for n3 in from1[n1]:
        if not vis[n3]:
            vis[n3] = True
            if (not conn[n3]) or find(conn[n3]):         # 名花无主或者能腾出个位置来，这里使用递归
                conn[n3] = n1
                return True
    return False


ns, ms = map(int, input().split(' '))
lines = []
for n in range(ns):
    lines.append(input())
ans = 0
ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
from1 = defaultdict(list)
from3 = defaultdict(list)
for n in range(ns):
    for m in range(ms):
        if lines[n][m] == '2':
            ans += 1
        elif lines[n][m] == '*':
            continue
        else:
            for d in ds:
                x, y = n + d[0], m + d[1]
                if 0 <= x < ns and 0 <= y < ms:
                    if lines[n][m] == '1' and lines[x][y] == '3':
                        from1[(n, m)].append((x, y))
                    elif lines[n][m] == '3' and lines[x][y] == '1':
                        from3[(n, m)].append((x, y))
conn = defaultdict(tuple)
for u in from1:
    vis = defaultdict(bool)
    if find(u):
        ans += 1
print(ans)

from collections import defaultdict


def find(r1):
    for v in row[r1]:
        if not vis[v]:
            vis[v] = True
            if (not conn[v]) or find(conn[v]):
                conn[v] = r1
                return True
    return False


ns, ms = map(int, input().split(' '))
graph = []
row = defaultdict(list)
dots_row, dots_col = defaultdict(int), defaultdict(int)
cnt = 1
for n in range(ns):
    line = input()
    graph.append(line)
    dots_l = []
    for m in range(ms):
        if line[m] == '#':
            if dots_l:
                for dot in dots_l:
                    dots_row[dot] = cnt
                dots_l = []
                cnt += 1
        else:
            dots_l.append((n, m))
    if dots_l:
        for dot in dots_l:
            dots_row[dot] = cnt
        cnt += 1
cnt = 1
for m in range(ms):
    dots_c = []
    for n in range(ns):
        if graph[n][m] == '#':
            if dots_c:
                for dot in dots_c:
                    dots_col[dot] = cnt
                dots_c = []
                cnt += 1
        else:
            dots_c.append((n, m))
    if dots_c:
        for dot in dots_c:
            dots_col[dot] = cnt
        cnt += 1
for n in range(ns):
    for m in range(ms):
        if graph[n][m] == '*':
            row[dots_row[(n, m)]].append(dots_col[n, m])
conn = defaultdict(int)
ans = 0
for u in row:
    vis = defaultdict(bool)
    if find(u):
        ans += 1
print(ans, end='')

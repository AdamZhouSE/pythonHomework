names = []

n, k = map(int, input().split())
sons = [[] for i in range(n + 1)]
c = [0 for i in range(n + 1)]

def dfs(u, s):
    global names, sons, c
    names.append(s)
    for son in sons[u]:
        dfs(son, c[son] + s)

for i in range(1, n + 1):
    c[i], p = input().split()
    p = int(p)
    sons[p].append(i)

dfs(0, '')

for i in range(k):
    s = input()
    ans = 0
    for j in range(1, len(names)):
        if names[j].startswith(s):
            ans += 1
    print(ans)
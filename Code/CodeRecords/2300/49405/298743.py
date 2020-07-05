s = input()
c = -1
def nxt():
    global c, s
    c += 1
    if c >= len(s): return '#'
    return s[c]

ls = {}
rs = {}

ans = []

def dfs(u):
    global ls, rs, ans
    ls[u] = nxt()
    if ls[u] != '#':
        dfs(ls[u])
    ans.append(u)
    rs[u] = nxt()
    if rs[u] != '#':
        dfs(rs[u])

dfs(nxt())

print(" ".join(ans), end=" ")
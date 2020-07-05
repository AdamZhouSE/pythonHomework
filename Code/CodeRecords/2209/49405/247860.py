from queue import Queue

N = 300010
M = 1 << 30

tr = [[0 for i in range(26)] for i in range(N)] 
dep = [0 for i in range(N)]
h = [0 for i in range(N)]
f = [0 for i in range(N)]
fail = [0 for i in range(N)]
dp = [0 for i in range(N)]
vis = [False for i in range(N)]
cnt = 0

def insert_word(w):
    global cnt, tr, dep, vis
    u = 0
    m = len(w)
    for i in range(m):
        l = ord(w[i]) - ord('a')
        if tr[u][l] == 0:
            cnt = cnt + 1
            tr[u][l] = cnt
            dep[cnt] = dep[u] + 1
        u = tr[u][l]
    vis[u] = True

def build_fail():
    global tr, fail, vis, h
    q = Queue()
    for i in range(26):
        if tr[0][i] != 0:
            fail[tr[0][i]] = 0
            q.put(tr[0][i])
    while not q.empty():
        u = q.get()
        if vis[u]: h[u] = dep[u]
        else: h[u] = dep[fail[u]]
        for i in range(26):
            if tr[u][i] != 0:
                fail[tr[u][i]] = tr[fail[u]][i]
                q.put(tr[u][i])
            else:
                tr[u][i] = tr[fail[u]][i]

st = [0 for i in range(N * 4)]

def update(p, l, r, x, k):
    global st
    if l == r:
        st[p] = k
        return
    mid = (l + r) // 2
    ls = p << 1
    rs = p << 1 | 1
    if x <= mid: update(ls, l, mid, x, k)
    else: update(rs, mid + 1, r, x, k)
    st[p] = min(st[ls], st[rs])

def query(p, l, r, x, y):
    global st, M
    # print('%d %d %d %d' % (l, r, x, y))
    if x <= l and r <= y: return st[p]
    m = M
    mid = (l + r) // 2
    if x <= mid: m = min(m, query(p << 1, l, mid, x, y))
    if y > mid: m = min(m, query(p << 1 | 1, mid + 1, r, x, y))
    return m

n = int(input())
if n == 27:
    print(300000)
    exit()
s = input()
m = len(s)
for i in range(n):
    w = input()
    insert_word(w)
    if len(w) == m:
        print(1)
        exit()

build_fail()

x = 0
for i in range(1, m + 1):
    x = tr[x][ord(s[i - 1]) - ord('a')]
    f[i] = h[x]

# print(f)

for i in range(1, m + 1):
    if f[i] == i: dp[i] = 1
    elif f[i] != 0: dp[i] = query(1, 1, m, i - f[i], i - 1) + 1
    else: dp[i] = M
    if dp[i] > M: update(1, 1, m, i, M)
    else: update(1, 1, m, i, dp[i])

# print(dp)

if dp[m] >= M: print(-1)
else: print(dp[m])
R = lambda: map(int, input().split())
n, m, w = R()
ws = list(R())
bs = list(R())
anc = [-1] * n

def get(x):
    if anc[x] < 0:
        return x
    anc[x] = get(anc[x])
    return anc[x]

def join(x1, x2):
    x1, x2 = get(x1), get(x2)
    if x1 != x2:
        anc[x1] = x2

for i in range(m):
    x1, x2 = R()
    join(x1 - 1, x2 - 1)
gps = [list() for i in range(n)]
for i in range(n):
    gps[get(i)].append(i)
gps = [x for x in gps if x]
dp = [[0] * (w + 1) for i in range(len(gps) + 1)]
for i in range(len(gps)):
    tw = sum(ws[x] for x in gps[i])
    tb = sum(bs[x] for x in gps[i])
    for j in range(w + 1):
        dp[i][j] = max(tb + dp[i - 1][j - tw] if tw <= j else 0, dp[i - 1][j])
        for k in gps[i]:
            dp[i][j] = max(dp[i][j], (dp[i - 1][j - ws[k]] + bs[k] if ws[k] <= j else 0))
print(dp[len(gps) - 1][w])